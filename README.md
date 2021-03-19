# Data API Examples

Coding demo about data APIs, JavaScript, Python, web servers, web techonologies and an
ask-me-anything session with [David Beitey (@davidjb)](https://git.io/davidjb).

Delivered as part of an industry/educator partnership formed in the
[ICT Gateway to Industry Schools Program (GISP) initiative](https://qldictgisp.acs.org.au/).

## Get a copy

[![Scan me](url.svg)](https://github.com/davidjb/gisp-data-api)

Visit <https://github.com/davidjb/gisp-data-api> to either view,
download or take a git clone of the code from GitHub or scan the above QR code.

## Examples

* [HTML + JavaScript Koala Locations](map.html)
* [HTML + JavaScript Koala Locations Mashup with Wikipedia](map-mashup.html)
* [Python + HTML + JavaScript Koala Locations Web Server](map.py)

## Outline

* Intro — outline, ask questions, introduction
* Background — who I am, my experience
* [APIs (Application Programming Interfaces)](https://en.wikipedia.org/wiki/API):

  * Demo and walkthrough of [examples](#examples)
  * API = Bistro: walk in, line up, there is a defined menu of offerings

      * You ask for what you want, they make it and deliver it.
      * You don't mind/can't see or control how they make your spaghetti, just that you get it
      * Some places may offer flexibility (V, GF, etc) but you have to ask for it
      * Not every restaurant is the same

  * General outline: what they are and aren't, how they work

    * [REST (`Representational State Transfer`)](https://en.m.wikipedia.org/wiki/Representational_state_transfer) — software _style_ involving textual representation of
      _resources_ that allow reading/modification using a defined set of
      operations. In short, it's about using HTTP methods (GET/POST/PUT/DELETE
      etc) to access/change data on a remote server in a defined way.
      
      * REST ⋍ Roads: except all rules are "should"/"might", signs may be wrong/missing,
        traffic lights (may be wrong!), congestion, potholes, toll bridges,
        gated communities, roads may just _end_

  * Data formats + view examples:

    * `JSON` (most common/universal): [example](https://www.data.qld.gov.au/api/3/action/datastore_search?resource_id=8dbceb06-aa8f-411a-baae-13d66475fdd7&limit=5)
    * `XML`:
      [example](https://qldspatial.information.qld.gov.au/catalogueadmin/rest/document?id={40D75ED6-3959-41EB-A5C8-E563FA5B66CA})

  * Tools & documentation vary wildly between APIs

    * [Wikipedia API sandbox](https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&origin=*&prop=pageimages%7Cinfo%7Cdescription%7Cpageprops%7Cpageterms%7Cmapdata&titles=Phascolarctos%20cinereus&redirects=1&formatversion=2&piprop=original&inprop=url%7Cdisplaytitle)
    * [Koala WildNet data](https://www.data.qld.gov.au/dataset/wildnet-koala-locations/resource/8dbceb06-aa8f-411a-baae-13d66475fdd7)
    * ...or little/no documentation at all
    * ...or not an API at all ([BOM Cyclone Forecast example](http://www.bom.gov.au/qld/forecasts/cyclone.shtml))

  * Considerations

    * **All APIs are different**
    * Programming language / environment being using (Python, JavaScript, PHP, etc)
    * Versoning: APIs will often have v1, v2, etc in their URLs indicating structure
    * [CORS: Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing) - ability to load data across domains in browser
    * [Rate Limiting](https://en.wikipedia.org/wiki/Rate_limiting): limits on allowed requests, by user/computer/network
    * Access Control: some APIs require keys or paid access (e.g. Google Maps API)
    * Error Handling: code should expect & handle errors (network failure, API offline, invalid data, etc)
    * Caching: hitting same API repeatedly is wasteful, leverage browser or other cache

* Work Experience:

  * [JCU Research Portfolio](https://jcu.me) — [redesigned UI](https://research.jcu.io) [Python, web design, SQL, databases]
  * IoT — [Classroom on the Reef](https://www.jcu.edu.au/classroom-on-the-reef/livecams) and [live sensor data](https://cotr-data.jcu.edu.au)
  * Home Assistant for automation
  * Security & consulting: software analysis, vulnerability reporting to companies, reviewing their APIs

* Q&A Session: ask me anything; around the syllabus or anything else

* Shameless plugs:

  * [DevNQ](https://devnq.org) - community run, all-invlusive group for IT developers (events, hackathon on Townsville Show weekend in July, socials)
  * [Young ICT Explorers](https://www.youngictexplorers.net.au/) - yearly competition that students/schools can enter and win prizes
  * [TCC Big Ideas Youth Challenge](https://www.eventbrite.com.au/e/townsville-city-council-big-ideas-youth-challenge-tickets-142196669065) - 22 April 2021, one day event around innovation, entrepreneurship and change. Also a PD session held on the day prior for teachers.
