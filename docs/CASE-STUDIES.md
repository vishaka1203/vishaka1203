# Behind the engineering decisions

## URL Shortener

**Problem.** Make long URLs easier to share and resolve each short link to the original destination.

**Investigation.** The public implementation has two distinct operations. The API receives a long URL. A Next.js dynamic route handles visitors following a short link.

**Engineering decision.** I interpret the separation as a way to keep link creation independent from link resolution. The code shows the separation, while the rationale is inferred.

**Implementation.** The creation handler looks for an existing mapping with a parameterized query and generates an eight-character Nano ID for a new mapping. The dynamic route reads by short code, then returns a temporary redirect or a 404.

**Validation.** The handlers and MySQL adapter were inspected. The deployed page was captured while idle. Link creation, redirect reliability, collision behaviour, and load limits were outside this observation.

**Outcome.** A shareable short-link interface backed by stored URL mappings. [Creation API](https://github.com/vishaka1203/URL-Shortener/blob/main/pages/api/shorten.js) · [Dynamic page](https://github.com/vishaka1203/URL-Shortener/blob/main/pages/%5BshortUrl%5D.js)

## Curating Frames

**Problem.** Present editorial photography collections and handle website enquiries.

**Investigation.** Gallery content and enquiry submission follow separate paths. Collections use structured content. Enquiries are sent to a Next.js route handler.

**Engineering decision.** The portfolio case study documents keeping collection data independent of gallery components and separating validation from delivery.

**Implementation.** App Router pages render the portfolio and individual collections. The enquiry endpoint applies validation before sending a message through the configured email provider.

**Validation.** The gallery route and enquiry handler were inspected and the deployed homepage was captured. No real enquiry was submitted.

**Outcome.** New collections can be added through content changes. The server can report an unavailable delivery configuration to the visitor. [Gallery route](https://github.com/vishaka1203/curating-frames/blob/main/app/portfolio/%5Bslug%5D/page.tsx) · [Enquiry handler](https://github.com/vishaka1203/curating-frames/blob/main/app/api/enquiry/route.ts) · [Portfolio case study](https://vishaka-parab-portfolio.vercel.app/projects/curating-frames)

## React DOM

**Problem.** The numeric value `hyphenateLimitLines: 2` produced the invalid CSS length `2px`.

**Investigation.** The DOM assignment and server-rendered style attribute both consult a shared unitless property set.

**Engineering decision.** Use the existing set to correct both paths together.

**Implementation.** The fork patch adds one set entry and regression tests for both renderers.

**Validation.** Both new tests failed at baseline and passed with the patch. The three focused suites reported 752 passing tests in development and stable production runs. The full suite reported one hydration failure, which also reproduced on the baseline. Safari 18.2 confirmed the change in serialized HTML and reported the unprefixed property as unsupported.

**Outcome.** The independent patch is published on the fork. The browser observation was shared on the existing upstream PR. [Fork patch](https://github.com/vishaka1203/react/commit/66a4856ee5) · [Upstream comment](https://github.com/react/react/pull/38352#issuecomment-7172209660)
