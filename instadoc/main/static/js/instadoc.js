(function( undefined ) {
  Backbone.Model.prototype.url = function() {
    // Use the id if possible
    var url = this.id;

    // If there's no idAttribute, use the 'urlRoot'. Fallback to try to have the collection construct a url.
    // Explicitly add the 'id' attribute if the model has one.
    if ( !url ) {
      url = this.urlRoot;
      url = url || this.collection && ( _.isFunction( this.collection.url ) ? this.collection.url() : this.collection.url );

      if ( url && this.has( 'id' ) ) {
        url = addSlash( url ) + this.get( 'id' );
      }
    }

    url = url && addSlash( url );
    return url + "?" + this.urlFilter || null;
  };

  Backbone.Collection.prototype.url = function( models ) {
    var url = this.urlRoot || ( models && models.length && models[0].urlRoot );
    url = url && addSlash( url );

    // Build a url to retrieve a set of models. This assume the last part of each model's idAttribute
    // (set to 'resource_uri') contains the model's id.
    if ( models && models.length ) {
      var ids = _.map( models, function( model ) {
          var parts = _.compact( model.id.split( '/' ) );
          return parts[ parts.length - 1 ];
        });
      url += 'set/' + ids.join( ';' ) + '/';
    }

    return url + "?" + this.urlFilter || null;
  };

  var addSlash = function( str ) {
    return str + ( ( str.length > 0 && str.charAt( str.length - 1 ) === '/' ) ? '' : '/' );
  };
})();

(function(){
  window.Doc = Backbone.Model.extend({
    urlRoot: API_URL,
    urlFilter: API_FILTER,
    defaults: {
      display: true
    }
  });

  window.Docs = Backbone.Collection.extend({
    urlRoot: API_URL,
    urlFilter: API_FILTER,
    model: Doc,

    maybeFetch: function(options){
      if(this._fetched){
        options.success = options.success();
        this.trigger("change");
        return;
      }
      var self = this,
        successWrapper = function(success){
          return function(){
            self._fetched = true;
            success = success.apply(this, arguments);
          };
        };
      options.success = successWrapper(options.success);
      this.fetch(options);
    },

    refetch: function(id, options){
      model = new Doc({
        resource_uri: id
      });
      model.fetch(options);
    },

    search: function(letters) {
      var regex = "";
      if( letters !== "" ) {
        $.each(letters, function(l) { regex = regex + ".*" + letters[l];});
      }
      var pattern = new RegExp(regex, "i");

      $.each(this.models, function(i) {
        this.attributes.display = true;
        if (!pattern.test(this.get("item"))) {
          this.attributes.display = false;
        }
      });

      this.trigger("change");
    },

    displayed: function() {
      return _(this.filter(function(data) {
        return data.attributes.display === true;
      }));
    }

  });

  window.DetailApp = Backbone.View.extend({
    render: function(){
      $(this.el).html(ich.detail_template(this.model.toJSON()));
      return this;
    }
  });


  window.ListItem = Backbone.View.extend({
    tagName: 'li',

    events: {
      'click .permalink': 'detail'
    },

    initialize: function(){
      this.model.bind('change', this.render, this);
    },

    detail: function(e){
      app.router.trigger('route:detail', this.model.id);
      e.preventDefault();
    },

    render: function(){
      $(this.el).html(ich.list_item_template(this.model.toJSON()));
      return this;
    }
  });

  window.ListView = Backbone.View.extend({
    initialize: function(){
      _.bindAll(this, 'addOne', 'addAll');

      this.collection.bind('reset', this.addAll, this);
      this.collection.bind('change', this.addAll, this);
      this.views = [];
    },

    addAll: function(){
      this.views = [];
      this.collection.displayed().each(this.addOne);
    },

    addOne: function(item){
      var view = new ListItem({
        model: item
      });
      $(this.el).prepend(view.render().el);
      this.views.push(view);
    }

  });

  window.ListCountView = Backbone.View.extend({
    initialize: function(){
      _.bindAll(this, 'render');
      this.collection.bind('change', this.render, this);
    },

    render: function(){
      $(this.el).html(this.collection.displayed()._wrapped.length + " Item(s)");
      return this;
    }
  });

  window.ListApp = Backbone.View.extend({
    events: {
      'keyup': 'search'
    },

    search: function(letter){
      $('#items').html('');
      var letters = this.$('#search').val();
      this.collection.search(letters);
    },

    render: function(){
      $(this.el).html(ich.list_template({}));
      this.list = new ListView({
        collection: this.collection,
        el: this.$('#items')
      });

      this.list_count = new ListCountView({
        collection: this.collection,
        el: this.$('#count')
      });

      this.collection.trigger("change");
      return this;
    }
  });

  window.Router = Backbone.Router.extend({
    routes: {
      '': 'list'
    },

    detail: function(){},

    list: function(){}
  });

  $(function(){
    window.app = window.app || {};
    app.router = new Router();
    app.docs = new Docs();
    app.list = new ListApp({
      el: $("#sidebar"),
      collection: app.docs
    });
    app.detail = new DetailApp({
      el: $("#detail")
    });
    app.router.bind('route:list', function(){
      app.docs.maybeFetch({
        success: _.bind(app.list.render, app.list)
      });
    });
    app.router.bind('route:detail', function(id){
      app.docs.refetch(id, {
        success: function(model){
          app.detail.model = model;
          app.detail.render();
        }
      });
    });

    Backbone.history.start({
      silent: app.loaded
    });
  });
})();

