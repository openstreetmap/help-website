+++
type = "question"
title = "how to perfom a request with different values for the location / area"
description = '''new to osm - and all the corresponding things like requests done with overpass and thelike  update: this thread is related to the thread https://help.openstreetmap.org/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser where i perform a request to the overpass-API-endpoi...'''
date = "2014-06-12T21:29:00Z"
lastmod = "2014-06-12T23:51:00Z"
weight = 33929
keywords = [ "xapi", "php", "osm", "mysql" ]
aliases = [ "/questions/33929" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to perfom a request with different values for the location / area](/questions/33929/how-to-perfom-a-request-with-different-values-for-the-location-area)

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
<span id="post-33929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>new to osm - and all the corresponding things like requests done with overpass and thelike</p>
<p>update: this thread is related to the thread <a href="/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser">https://help.openstreetmap.org/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser</a></p>
<p>where i perform a request to the overpass-API-endpoint. All goes well - but i want to have</p>
<p>a. the results stored within a mysql-database b. perform a request with another area-definition....</p>
<p>see more at the above mentioned thread:</p>
<p>how to perform a request - note i do them with PHP</p>
<pre><code>$query = &#39;node
  [&quot;amenity&quot;~&quot;.*&quot;]
  (38.415938460513274,16.06338500976562,39.52205163048525,17.51220703125);
out;&#39;;</code></pre>
<p>what if i replace this with the following</p>
<pre><code>$query = &#39;node
  [&quot;addr:postcode&quot;~&quot;RM12&quot;]
  (51.5557914,0.2118915,51.5673083,0.2369398);
   node
  (around:1000)
  [&quot;amenity&quot;~&quot;fast_food&quot;];
           out;&#39;;</code></pre>
<p>cf: <a href="https://wiki.openstreetmap.org/wiki/Xapi">https://wiki.openstreetmap.org/wiki/Xapi</a></p>
<p>well can i enter values for countries as well what if i want to have all schools from a certain country:<br />
</p>
<pre><code>$query = &#39;node
  [&quot;addr:country&quot;~&quot;Brasil&quot;]
   node
  [&quot;amenity&quot;~&quot;school&quot;];
           out;&#39;;</code></pre>
<p><strong>question</strong> - can i do like mentioned above - can i perfom such requests?</p>
<p>please set me straight if my question is not concise and concrete enough</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 21:29</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '14, 22:28</strong> </span></p>
</div>
</div>
<div id="comments-container-33929" class="comments-container">
<span id="33930"></span>
<div id="comment-33930" class="comment">
<div id="post-33930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Are you trying to use XAPI or Overpass? You've referenced the XAPI wiki page and are quoting what looks like overpass queries. Also, you've not said what (this time) your end goal is.</p>
<p>It might help to take a step back and document somewhere (perhaps on a personal wiki page?) what you're trying to do, why you're trying to do it, what you've tried so far, what you expected to happen, and what actually did happen.</p>
<p>This page here is about software bug reporting:</p>
<p><a href="http://www.joelonsoftware.com/articles/fog0000000029.html">http://www.joelonsoftware.com/articles/fog0000000029.html</a></p>
<p>but you might find it helpful all the same.</p>
</div>
<div id="comment-33930-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 21:56)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33933"></span>
<div id="comment-33933" class="comment">
<div id="post-33933-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>update: thank you for the respond! this thread is related to the thread <a href="/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser">https://help.openstreetmap.org/questions/33926/osm-overpass-api-with-php-simplexml-minor-changes-to-the-parser</a></p>
<p>where i perform a request to the overpass-API-endpoint. All goes well - but i want to have</p>
<p>a. the results stored within a mysql-database b. perform a request with another area-definition....</p>
<p>see more at the above mentioned thread:</p>
</div>
<div id="comment-33933-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 22:29)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="33937"></span>
<div id="comment-33937" class="comment">
<div id="post-33937-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear SomeQoneElse - again me. well since i am learing while working with the scripts i have create a wiki-page - here i collect all the ideas and good things that i collect in the internet. see the above mentioned question - in other words - rephrased <a href="https://wiki.openstreetmap.org/wiki/PHP_und_Overpass">https://wiki.openstreetmap.org/wiki/PHP_und_Overpass</a></p>
<p>love to hear from you. Dont hesitate to add your ideas - either here or at the wikipage</p>
</div>
<div id="comment-33937-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 23:51)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-33929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33929-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

