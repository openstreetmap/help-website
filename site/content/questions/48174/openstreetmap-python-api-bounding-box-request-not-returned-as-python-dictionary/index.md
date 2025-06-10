+++
type = "question"
title = "OpenStreetMap Python API Bounding Box Request not Returned as Python Dictionary"
description = '''Apologies if this is a dense question I am green with OSM. When I make an API bounding box call like below: import overpass  # bounding box coordinates min_long = min(longs) min_lat = min(lats) max_long = max(longs) max_lat = max(lats)  # query overpass within OpenStreetMap api = overpass.API() map_...'''
date = "2016-02-16T16:46:00Z"
lastmod = "2016-02-16T19:29:00Z"
weight = 48174
keywords = [ "python", "overpass", "overpassapi", "overpass-api" ]
aliases = [ "/questions/48174" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetMap Python API Bounding Box Request not Returned as Python Dictionary](/questions/48174/openstreetmap-python-api-bounding-box-request-not-returned-as-python-dictionary)

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
<span id="post-48174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48174-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Apologies if this is a dense question I am green with OSM.</p>
<p>When I make an API bounding box call like below:</p>
<pre><code>import overpass
&#10;# bounding box coordinates
min_long = min(longs)
min_lat = min(lats)
max_long = max(longs)
max_lat = max(lats)
&#10;# query overpass within OpenStreetMap
api = overpass.API()
map_query = overpass.MapQuery(min_lat,min_long,max_lat,max_long)
response = api.Get(map_query)</code></pre>
<p>The output is not wrapped in a Python dictionary like <a href="https://help.openstreetmap.org/questions/47075/overpass-api-python-save-tags">here</a>. The response appears to be xml.</p>
<p>Anybody have an idea of what is going on here? Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Feb '16, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/8f93455ec0ee39ebb69fc73f94c04d77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jlgutenson&#39;s gravatar image" />
<p><span>jlgutenson</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jlgutenson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48174" class="comments-container">
<span id="48180"></span>
<div id="comment-48180" class="comment">
<div id="post-48180-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/180980/openstreetmap-python-api-bounding-box-request">https://gis.stackexchange.com/questions/180980/openstreetmap-python-api-bounding-box-request</a></p>
</div>
<div id="comment-48180-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 18:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48174-form-container" class="comment-form-container">
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

<span id="48175"></span>

<div id="answer-container-48175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48175-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API supports different <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Choose_file_format">file formats</a> (currently XML, JSON and CSV). According to a quick search you seem to be using <a href="https://github.com/mvexel/overpass-api-python-wrapper">Overpass API python wrapper</a>. The README explains that you can call <code>Get()</code> with a <code>responseformat</code> parameter for choosing the file format. So try calling <code>api.Get(map_query, responseformat="json")</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '16, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48175" class="comments-container">
<span id="48177"></span>
<div id="comment-48177" class="comment">
<div id="post-48177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've seen that. Interestingly though, I keep getting the error <code>TypeError: Get() got an unexpected keyword argument 'responseformat'</code> for any format type.</p>
</div>
<div id="comment-48177-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 18:16)</span> <span class="comment-user userinfo">jlgutenson</span>
</div>
</div>
<span id="48179"></span>
<div id="comment-48179" class="comment">
<div id="post-48179-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just tried the example from the README with the latest version on GitHub and it works. It even uses "geojson" as default file format. But specifying <code>responseformat="json"</code> or <code>responseformat="xml"</code> also works fine.</p>
</div>
<div id="comment-48179-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 18:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48183"></span>
<div id="comment-48183" class="comment">
<div id="post-48183-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting <a href="http://help.openstreetmap.org/users/158/scai">@scai</a>, are you using version 0.3.1 as well? Sounds like something with my installation is off.:-/</p>
</div>
<div id="comment-48183-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 18:34)</span> <span class="comment-user userinfo">jlgutenson</span>
</div>
</div>
<span id="48184"></span>
<div id="comment-48184" class="comment">
<div id="post-48184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using the master branch which seems to be 0.3.1 according to <em>__init__.py</em>.</p>
</div>
<div id="comment-48184-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 18:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48175-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48185"></span>

<div id="answer-container-48185" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Turns out the pip installation of the Python Overpass API is different than the current version on github. If anyone else encounters this problem, just install the github version instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Feb '16, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/8f93455ec0ee39ebb69fc73f94c04d77?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jlgutenson&#39;s gravatar image" />
<p><span>jlgutenson</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jlgutenson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48185" class="comments-container">
&#10;</div>
<div id="comment-tools-48185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48185-form-container" class="comment-form-container">
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

