+++
type = "question"
title = "own Nominatim server not working with geopy"
description = '''I have a database of over 6k entries of addresses need for geocoding, thus I have installed nominatim server with docker for geocoding work. It works as it should in the web form on the &#x27;localhost:8080&#x27;. However, when I try to query with geopy in jupyter. It throws error all the time. My Jupyter cod...'''
date = "2017-07-28T19:22:00Z"
lastmod = "2017-07-28T23:39:00Z"
weight = 57336
keywords = [ "nominatim" ]
aliases = [ "/questions/57336" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [own Nominatim server not working with geopy](/questions/57336/own-nominatim-server-not-working-with-geopy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57336-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a database of over 6k entries of addresses need for geocoding, thus I have installed nominatim server with docker for geocoding work. It works as it should in the web form on the 'localhost:8080'.</p>
<p>However, when I try to query with geopy in jupyter. It throws error all the time.</p>
<p>My Jupyter code:</p>
<pre><code>from geopy.geocoder import Nominatim
nom=Nominatim(domain=&#39;http://localhost:8080&#39;)
nom.geocode(&#39;some address&#39;) #the address works on the public server</code></pre>
<p>The error stack:</p>
<pre><code>gaierror                                  Traceback (most recent call last)
/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
   1253             try:
-&gt; 1254                 h.request(req.get_method(), req.selector, req.data, headers)
   1255             except OSError as err: # timeout error
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in request(self, method, url, body, headers)
   1105         &quot;&quot;&quot;Send a complete request to the server.&quot;&quot;&quot;
-&gt; 1106         self._send_request(method, url, body, headers)
   1107
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in _send_request(self, method, url, body, headers)
   1150             body = _encode(body, &#39;body&#39;)
-&gt; 1151         self.endheaders(body)
   1152
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in endheaders(self, message_body)
   1101             raise CannotSendHeader()
-&gt; 1102         self._send_output(message_body)
   1103
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in _send_output(self, message_body)
    933 
--&gt; 934         self.send(msg)
    935         if message_body is not None:
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in send(self, data)
    876             if self.auto_open:
--&gt; 877                 self.connect()
    878             else:
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in connect(self)
   1251 
-&gt; 1252             super().connect()
   1253
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/http/client.py in connect(self)
    848         self.sock = self._create_connection(
--&gt; 849             (self.host,self.port), self.timeout, self.source_address)
    850         self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py in create_connection(address, timeout, source_address)
    692     err = None
--&gt; 693     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
    694         af, socktype, proto, canonname, sa = res
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/socket.py in getaddrinfo(host, port, family, type, proto, flags)
    731     addrlist = []
--&gt; 732     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
    733         af, socktype, proto, canonname, sa = res
&#10;gaierror: [Errno 8] nodename nor servname provided, or not known
&#10;During handling of the above exception, another exception occurred:
&#10;URLError                                  Traceback (most recent call last)
/Users/nmbqz/.virtualenvs/scrapy/lib/python3.5/site-packages/geopy/geocoders/base.py in _call_geocoder(self, url, timeout, raw, requester, deserializer, **kwargs)
    142         try:
--&gt; 143             page = requester(req, timeout=(timeout or self.timeout), **kwargs)
    144         except Exception as error: # pylint: disable=W0703
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
    162         opener = _opener
--&gt; 163     return opener.open(url, data, timeout)
    164
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in open(self, fullurl, data, timeout)
    465 
--&gt; 466         response = self._open(req, data)
    467
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in _open(self, req, data)
    483         result = self._call_chain(self.handle_open, protocol, protocol +
--&gt; 484                                   &#39;_open&#39;, req)
    485         if result:
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in _call_chain(self, chain, kind, meth_name, *args)
    443             func = getattr(handler, meth_name)
--&gt; 444             result = func(*args)
    445             if result is not None:
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in https_open(self, req)
   1296             return self.do_open(http.client.HTTPSConnection, req,
-&gt; 1297                 context=self._context, check_hostname=self._check_hostname)
   1298
&#10;/usr/local/Cellar/python3/3.5.2_3/Frameworks/Python.framework/Versions/3.5/lib/python3.5/urllib/request.py in do_open(self, http_class, req, **http_conn_args)
   1255             except OSError as err: # timeout error
-&gt; 1256                 raise URLError(err)
   1257             r = h.getresponse()
&#10;URLError: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt;
&#10;During handling of the above exception, another exception occurred:
&#10;GeocoderServiceError                      Traceback (most recent call last)
&lt;ipython-input-141-ad9610064de4&gt; in &lt;module&gt;()
----&gt; 1 nom.geocode(&#39;Revontulentie 11&#39;)
&#10;/Users/nmbqz/.virtualenvs/scrapy/lib/python3.5/site-packages/geopy/geocoders/osm.py in geocode(self, query, exactly_one, timeout, addressdetails, language, geometry)
    191         logger.debug(&quot;%s.geocode: %s&quot;, self.__class__.__name__, url)
    192         return self._parse_json(
--&gt; 193             self._call_geocoder(url, timeout=timeout), exactly_one
    194         )
    195
&#10;/Users/nmbqz/.virtualenvs/scrapy/lib/python3.5/site-packages/geopy/geocoders/base.py in _call_geocoder(self, url, timeout, raw, requester, deserializer, **kwargs)
    169                 if &quot;timed out&quot; in message:
    170                     raise GeocoderTimedOut(&#39;Service timed out&#39;)
--&gt; 171             raise GeocoderServiceError(message)
    172 
    173         if hasattr(page, &#39;getcode&#39;):
&#10;GeocoderServiceError: [Errno 8] nodename nor servname provided, or not known</code></pre>
<p>Appreciate some clues!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '17, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/7b5b9afd501c8b84fe1086ea959b4676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jimmy_Jin&#39;s gravatar image" />
<p><span>Jimmy_Jin</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jimmy_Jin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57336" class="comments-container">
&#10;</div>
<div id="comment-tools-57336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57336-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57342"></span>

<div id="answer-container-57342" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57342-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jimmy_Jin has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm pretty sure your local Nominatim installation runs on <a href="http://localhost:8080/nominatim/search?format=jsonv2&amp;q=Berlin&amp;limit=1">http://localhost:8080/nominatim/search?format=jsonv2&amp;q=Berlin&amp;limit=1</a> Note the <code>/nominatim</code> part of the path that the server nominatim.openstreetmap.org is missing.</p>
<p>Try</p>
<p><code>nom = Nominatim(domain='localhost:8080/nominatim', scheme='http')</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '17, 23:17</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '17, 23:22</strong> </span></p>
</div>
</div>
<div id="comments-container-57342" class="comments-container">
<span id="57343"></span>
<div id="comment-57343" class="comment">
<div id="post-57343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>by try I mean that worked when I ran it against my local Nominatim</p>
</div>
<div id="comment-57343-info" class="comment-info">
<span class="comment-age">(28 Jul '17, 23:27)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="57345"></span>
<div id="comment-57345" class="comment">
<div id="post-57345-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>My link does not actually contain nomination : 'http://127.0.0.1:8080/search.php?q=Berlin&amp;polygon=1&amp;viewbox=' I find the wrong part is: nom=Nominatim(domain='http://localhost:8080')</p>
<p>the correct form is</p>
<p>nom=Nominatim(domain='localhost:8080', scheme='http')</p>
<p>I got hint from your answer, thanks.</p>
</div>
<div id="comment-57345-info" class="comment-info">
<span class="comment-age">(28 Jul '17, 23:39)</span> <span class="comment-user userinfo">Jimmy_Jin</span>
</div>
</div>
</div>
<div id="comment-tools-57342" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57342-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

