+++
type = "question"
title = "Comparing http.request.method==GET and File &gt;Export Objects&gt;HTTP"
description = '''I tried to open a website that is hosted on Port 80.I captured all the packets related to that particular Site.Here,I am seeing a mismatch between no.of GET Requests initiated(Showing 95) vs Object list in File&amp;gt;Export Objects &amp;gt;HTTP(Showing 28)  Is this a real discrepancy? I am under the impres...'''
date = "2013-03-06T19:53:00Z"
lastmod = "2013-03-06T21:35:00Z"
weight = 19258
keywords = [ "objects", "get" ]
aliases = [ "/questions/19258" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Comparing http.request.method==GET and File &gt;Export Objects&gt;HTTP](/questions/19258/comparing-httprequestmethodget-and-file-export-objectshttp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19258-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19258-score" class="post-score" title="current number of votes">0</div><span id="post-19258-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to open a website that is hosted on Port 80.I captured all the packets related to that particular Site.Here,I am seeing a mismatch between no.of GET Requests initiated(Showing 95) vs Object list in File&gt;Export Objects &gt;HTTP(Showing 28) Is this a real discrepancy? I am under the impression that each GET Request is an object and hence both should be same.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-objects" rel="tag" title="see questions tagged &#39;objects&#39;">objects</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '13, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-19258" class="comments-container"></div><div id="comment-tools-19258" class="comment-tools"></div><div class="clear"></div><div id="comment-19258-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19259"></span>

<div id="answer-container-19259" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19259-score" class="post-score" title="current number of votes">1</div><span id="post-19259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krishnayeddula has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am under the impression that each GET Request is an object</p></blockquote><p>Not necessarily:</p><pre><code>$ telnet www.wireshark.org 80
Trying 174.137.42.75...
Connected to www.wireshark.org.
Escape character is &#39;^]&#39;.
GET /purplemonkeydishwasher HTTP/1.1
Host: www.wireshark.org

HTTP/1.1 404 Not Found
Date: Thu, 07 Mar 2013 03:58:22 GMT
Server: Apache/2
Last-Modified: Wed, 06 Mar 2013 23:28:43 GMT
Accept-Ranges: bytes
Content-Length: 1540
Vary: Accept-Encoding
X-Slogan: Sniff free or die.
Cache-control: max-age=0, no-cache, no-store
Content-Type: text/html

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;!DOCTYPE html
  PUBLIC &quot;-//W3C//DTD XHTML 1.0 Strict//EN&quot;
  &quot;DTD/xhtml1-strict.dtd&quot;&gt;
&lt;html xmlns=&quot;http://www.w3.org/1999/xhtml&quot; xml:lang=&quot;en&quot; lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Oops&lt;/title&gt;
  &lt;style type=&quot;text/css&quot;&gt;</code></pre><p><em>commented-out CSS style sheet elided</em></p><pre><code>  &lt;/style&gt;
&lt;/head&gt;
&lt;style type=&quot;text/css&quot; media=&quot;screen&quot;&gt;
@import url(&quot;/css/jqui/ui.all.css&quot;);
&lt;/style&gt;
&lt;body&gt;
&lt;div id=&quot;main&quot;&gt;
&lt;a href=&quot;http://www.wireshark.org/&quot;&gt;&lt;img src=&quot;/image/wsbadge64.png&quot; alt=&quot;&quot;&gt;&lt;/img&gt;&lt;/a&gt;
&lt;h1&gt;Oops.&lt;/h1&gt;
&lt;div class=&quot;clear&quot;&gt;&lt;/div&gt;
&lt;p&gt;
We couldn&#39;t find the file you requested. If you&#39;re lost, you might try:
&lt;/p&gt;
&lt;ul style=&quot;list-style-type: none&quot;&gt;
  &lt;li&gt;&lt;a href=&quot;/&quot;&gt;The main page&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;&lt;a href=&quot;/download.html&quot;&gt;The download page&lt;/a&gt;&lt;/li&gt;
  &lt;li&gt;&lt;a href=&quot;/docs/&quot;&gt;The documentation&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;div class=&quot;clear&quot;&gt;&lt;/div&gt;
&lt;!-- Shamelessly stolen from http://www.stevefu.net/hostedstuff/mine/pics/im-in-ur-servr-sniffin-ur-paketz.jpg --&gt;
&lt;img src=&quot;/image/im-in-ur-servr-sniffin-ur-paketz.jpg&quot; style=&quot;margin-left: auto; margin-right: auto&quot; alt=&quot;&quot;&gt;
&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre><p>That's a GET request, but it returned an error; I guess you could argue that the error page is an object, but it's normally not an object that somebody <em>intended</em> to get.</p><p>Did any of the GET requests get a reply code <em>other</em> than 200? For example, did they get errors (4xx or 5xx), or a 304 "Not modified", or a 302 "Moved temporarily", or a 301 "Moved permanently", or...?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 20:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19259" class="comments-container"><span id="19263"></span><div id="comment-19263" class="comment"><div id="post-19263-score" class="comment-score"></div><div class="comment-text"><p>Yes all those missed in Objects got response code 304 Not Modified. Thanks for letting me know the undercurrent behavior.Clearing the browser cache and repeating the test worked.</p></div><div id="comment-19263-info" class="comment-info"><span class="comment-age">(06 Mar '13, 21:26)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="19264"></span><div id="comment-19264" class="comment"><div id="post-19264-score" class="comment-score"></div><div class="comment-text"><p>Ah, yes, good old If-Modified-Since.</p></div><div id="comment-19264-info" class="comment-info"><span class="comment-age">(06 Mar '13, 21:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-19259" class="comment-tools"></div><div class="clear"></div><div id="comment-19259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

