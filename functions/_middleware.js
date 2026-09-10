const GA_MEASUREMENT_ID = "G-T47EEK5EH0";

export async function onRequest(context) {
  const response = await context.next();
  const contentType = response.headers.get("content-type") || "";

  if (!contentType.includes("text/html")) {
    return response;
  }

  return new HTMLRewriter()
    .on("head", {
      element(element) {
        element.append(
          `<script async src="https://www.googletagmanager.com/gtag/js?id=${GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '${GA_MEASUREMENT_ID}');
</script>`,
          { html: true }
        );
      }
    })
    .transform(response);
}
