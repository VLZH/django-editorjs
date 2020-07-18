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
   * @param {HTMLDivElement} field_wrapper
   */
  function initEditorJsField(field_wrapper) {
    var holder_el = field_wrapper.querySelector("[data-editorjs-holder]");
    var input_el = field_wrapper.querySelector("[data-editorjs-input]");
    var config_el = field_wrapper.querySelector("[data-editorjs-config]");
    var config = JSON.parse(config_el.innerHTML.trim());

    const editor = new EditorJS({
      holder: holder_el,
      tools: {
        Image: extractToolConfig(config, "Image", {
          class: ImageTool,
          inlineToolbar: true,
        }),
        Header: extractToolConfig(config, "Header", {
          class: Header,
        }),
        Checklist: extractToolConfig(config, "Checklist", {
          class: Checklist,
          inlineToolbar: true,
        }),
        List: extractToolConfig(config, "List", {
          class: List,
          inlineToolbar: true,
        }),
        Quote: extractToolConfig(config, "Quote", {
          class: Quote,
          inlineToolbar: true,
        }),
        Raw: extractToolConfig(config, "Raw", {
          class: RawTool,
        }),
        Embed: extractToolConfig(config, "Embed", {
          class: Embed,
          inlineToolbar: true,
        }),
        Delimiter: extractToolConfig(config, "Delimiter", {
          class: Delimiter,
        }),
        Warning: extractToolConfig(config, "Warning", {
          class: Warning,
          inlineToolbar: true,
        }),
        Link: extractToolConfig(config, "Link", {
          class: LinkTool,
        }),
        Marker: extractToolConfig(config, "Marker", {
          class: Marker,
        }),
        Attaches: extractToolConfig(config, "Attaches", {
          class: AttachesTool,
        }),
        Table: extractToolConfig(config, "Table", {
          class: Table,
          inlineToolbar: true,
        }),
      },
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
