(function () {
  /**
   * @param {Object} config
   * @param {String} tool
   * @param {Object} default_config
   */
  function extractToolConfig(config, tool, default_config) {
    var result = Object.assign({}, default_config);
    if (config && config.tools && config.tools[tool]) {
      if (config.tools[tool].disabled) {
        return undefined;
      }
      Object.assign(result, config.tools[tool]);
    }
    return result;
  }

  /**
   * @param {Object} config
   * @param {String} tool
   */
  function isDisabled(config, tool) {
    return !!(
      config &&
      config.tools &&
      config.tools[tool] &&
      config.tools[tool].disabled
    );
  }

  /**
   * @param {HTMLDivElement} field_wrapper
   */
  function initEditorJsField(field_wrapper) {
    var holder_el = field_wrapper.querySelector("[data-editorjs-holder]");
    var input_el = field_wrapper.querySelector("[data-editorjs-input]");
    var config_el = field_wrapper.querySelector("[data-editorjs-config]");
    var config = JSON.parse(config_el.innerHTML.trim());
    var tools = {};
    if (!isDisabled(config, "Image")) {
      tools.Image = extractToolConfig(config, "Image", {
        class: ImageTool,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "Header")) {
      tools.Header = extractToolConfig(config, "Header", {
        class: Header,
      });
    }
    if (!isDisabled(config, "Checklist")) {
      tools.Checklist = extractToolConfig(config, "Checklist", {
        class: Checklist,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "List")) {
      tools.List = extractToolConfig(config, "List", {
        class: List,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "Quote")) {
      tools.Quote = extractToolConfig(config, "Quote", {
        class: Quote,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "Raw")) {
      tools.Raw = extractToolConfig(config, "Raw", {
        class: RawTool,
      });
    }
    if (!isDisabled(config, "Embed")) {
      tools.Embed = extractToolConfig(config, "Embed", {
        class: Embed,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "Delimiter")) {
      tools.Delimiter = extractToolConfig(config, "Delimiter", {
        class: Delimiter,
      });
    }
    if (!isDisabled(config, "Warning")) {
      tools.Warning = extractToolConfig(config, "Warning", {
        class: Warning,
        inlineToolbar: true,
      });
    }
    if (!isDisabled(config, "Link")) {
      tools.Link = extractToolConfig(config, "Link", {
        class: LinkTool,
      });
    }
    if (!isDisabled(config, "Marker")) {
      tools.Marker = extractToolConfig(config, "Marker", {
        class: Marker,
      });
    }
    if (!isDisabled(config, "Attaches")) {
      tools.Attaches = extractToolConfig(config, "Attaches", {
        class: AttachesTool,
      });
    }
    if (!isDisabled(config, "Table")) {
      tools.Table = extractToolConfig(config, "Table", {
        class: Table,
        inlineToolbar: true,
      });
    }

    const editor = new EditorJS({
      holder: holder_el,
      tools: tools,
      data:
        (input_el.value &&
          input_el.value.trim() &&
          JSON.parse(input_el.value.trim())) ||
        undefined,
      onChange: function () {
        editor
          .save()
          .then(function (outputData) {
            console.log(JSON.stringify(outputData));
            input_el.value = JSON.stringify(outputData);
          })
          .catch(function (error) {
            console.log("Saving failed: ", error);
          });
      },
    });
  }

  window.addEventListener("load", function () {
    var editor_wrappers = document.querySelectorAll("[data-editorjs-wrapper]");
    editor_wrappers.forEach(initEditorJsField);
  });
})();
