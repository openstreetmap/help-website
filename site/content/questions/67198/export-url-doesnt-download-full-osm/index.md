+++
type = "question"
title = "Export URL Doesn&#x27;t Download Full OSM"
description = '''I am trying to write up a MATLAB function to go to a user specified location on Opens Street Maps and return the OSM file using websave(). This works but the OSM I receive is nothing more than the xml and osm version and box bounds. How do I download the nodes and tags as if I were on Open Street&#x27;s ...'''
date = "2018-12-14T16:42:00Z"
lastmod = "2018-12-19T07:05:00Z"
weight = 67198
keywords = [ "export", "matlab" ]
aliases = [ "/questions/67198" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Export URL Doesn't Download Full OSM](/questions/67198/export-url-doesnt-download-full-osm)

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
<span id="post-67198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67198-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to write up a MATLAB function to go to a user specified location on Opens Street Maps and return the OSM file using websave(). This works but the OSM I receive is nothing more than the xml and osm version and box bounds. How do I download the nodes and tags as if I were on Open Street's site?</p>
<p>The URL I'm using is this: <a href="https://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145">https://api.openstreetmap.org/api/0.6/map?bbox=11.54,48.14,11.543,48.145</a></p>
<p>Update: What I'm attempting to do is simply execute the "Export" function that OpenStreetMap's website has but from MATLAB. The OSM files I download do not appear to have any nodes as shown below:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;osm version=&quot;0.6&quot; generator=&quot;CGImap 0.6.1 (1926 thorn-01.openstreetmap.org)&quot; copyright=&quot;OpenStreetMap and contributors&quot; attribution=&quot;https://www.openstreetmap.org/copyright&quot; license=&quot;http://opendatacommons.org/licenses/odbl/1-0/&quot;&gt;
 &lt;bounds minlat=&quot;48.1398000&quot; minlon=&quot;11.5402000&quot; maxlat=&quot;48.1402000&quot; maxlon=&quot;11.5402000&quot;/&gt;
&lt;/osm&gt;</code></pre>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-matlab" rel="tag" title="see questions tagged &#39;matlab&#39;">matlab</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Dec '18, 16:42</strong></p>
<img src="https://secure.gravatar.com/avatar/35ea97637fc08dfdde60934ba34c6996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jholland4134&#39;s gravatar image" />
<p><span>jholland4134</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jholland4134 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Dec '18, 07:03</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-67198" class="comments-container">
&#10;</div>
<div id="comment-tools-67198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67198-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="67216"></span>

<div id="answer-container-67216" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67216-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-67216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I notice that the min and max longitude above are the same.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Dec '18, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-67216" class="comments-container">
<span id="67272"></span>
<div id="comment-67272" class="comment">
<div id="post-67272-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks to nevw, I rechecked my code and noticed that I failed to expand my bounds. The rest appears to be fine.</p>
</div>
<div id="comment-67272-info" class="comment-info">
<span class="comment-age">(18 Dec '18, 22:47)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
<span id="67275"></span>
<div id="comment-67275" class="comment">
<div id="post-67275-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: @jholland4132: Please could you <a href="/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered">mark an answer as accepted</a> if your problem is solved now?</p>
</div>
<div id="comment-67275-info" class="comment-info">
<span class="comment-age">(19 Dec '18, 07:05)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67216" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67216-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67200"></span>

<div id="answer-container-67200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67200-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That URL is returning an OpenStreetMap XML file(6MB), and it includes nodes.. You can read information on the <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">XML format of OSM</a>. It's possible that Matlab just doesn't (automatically) understand what kind of XML it is, and how to process it.</p>
<p>If you're interested in only reading the data from OpenStreetMap, you might want to take a look at the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. This has several features so you can query specific data in the area, or get different file formats returned.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '18, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/f846f21cfbcf60a35e1f69c2cc74df77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LivingWithDragons&#39;s gravatar image" />
<p><span>LivingWithDr...</span><br />
<span class="score" title="524 reputation points">524</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LivingWithDragons has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-67200" class="comments-container">
<span id="67212"></span>
<div id="comment-67212" class="comment">
<div id="post-67212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the assistance.</p>
</div>
<div id="comment-67212-info" class="comment-info">
<span class="comment-age">(15 Dec '18, 15:21)</span> <span class="comment-user userinfo">jholland4134</span>
</div>
</div>
</div>
<div id="comment-tools-67200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67200-form-container" class="comment-form-container">
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

