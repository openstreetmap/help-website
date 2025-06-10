+++
type = "question"
title = "Using OpenStreetMap with keyword search bookmarks in Firefox"
description = '''Firefox has a function where you can set up bookmarks that can be called by typing a keyword in the address bar. For example: If I made a bookmark to Wikipedia and assign that bookmark the keyword &quot;w&quot;, then I just have to go the address bar, type &quot;w&quot;, and hit enter. Firefox fills in the address. Fir...'''
date = "2011-11-23T08:28:00Z"
lastmod = "2013-04-25T12:56:00Z"
weight = 9196
keywords = [ "search", "nominatim", "firefox" ]
aliases = [ "/questions/9196" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using OpenStreetMap with keyword search bookmarks in Firefox](/questions/9196/using-openstreetmap-with-keyword-search-bookmarks-in-firefox)

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
<span id="post-9196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9196-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Firefox has a function where you can set up bookmarks that can be called by typing a keyword in the address bar. For example: If I made a bookmark to Wikipedia and assign that bookmark the keyword "w", then I just have to go the address bar, type "w", and hit enter. Firefox fills in the address.</p>
<p>Firefox also supports text replacement after the keyword is entered. So say, instead of Wikipedia's address, I bookmarked <a href="http://en.wikipedia.org/wiki/Special:Search?search=%s">http://en.wikipedia.org/wiki/Special:Search?search=%s</a> (note the %s), I could type "w Jimmy Whales" into my address bar and it would go to the link "http://en.wikipedia.org/wiki/Special:Search?search=Jimmy+Whales" Which would then immediately go to <a href="http://en.wikipedia.org/wiki/Jimmy_Whales">http://en.wikipedia.org/wiki/Jimmy_Whales</a></p>
<p>Lots of online services provide support for this kind of hackery, and Nominatim is no exception... but I can't figure out how to get nominatim's search working with OpenStreetMap's map. Nominatims map seems to be different from OSM's, even though I'm sure they are pulling from the same data, OSM's map seems to work faster and provides more landmarks. Is there any way I can use Firefox's keyword search to get nominatim's results on OSM's map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '11, 08:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f947d945ccd9f9e8be5deab92abb41a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghoti&#39;s gravatar image" />
<p><span>ghoti</span><br />
<span class="score" title="116 reputation points">116</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghoti has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9196" class="comments-container">
&#10;</div>
<div id="comment-tools-9196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9196-form-container" class="comment-form-container">
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

<span id="9198"></span>

<div id="answer-container-9198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9198-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-9198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is an easy way to get search keywords into Firefox if the website offers an <a href="http://wikipedia.org/wiki/OpenSearch">OpenSearch</a> description:</p>
<ol>
<li>go to the website</li>
<li>click on the drop-down icon in your search bar (in a default firefox installation, this is located in the <a href="http://en.wikipedia.org/wiki/File:Dewiki-searchplugin-blueish-autodiscovery.png">upper right corner</a>)</li>
<li>choose the "Add [Name of the Search]" entry</li>
<li>click on the drop-down icon again and choose the "manage search engines" entry</li>
<li>assign a keyword to the new search engine</li>
</ol>
<p>Most OpenStreetMap services offer this feature - including <a href="http://osm.org"></a><a href="http://osm.org">osm.org</a> -, so there is hardly a reason to construct search bookmarks manually.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '11, 09:33</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '11, 09:38</strong> </span></p>
</div>
</div>
<div id="comments-container-9198" class="comments-container">
<span id="9204"></span>
<div id="comment-9204" class="comment">
<div id="post-9204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate you feel this is a bad way to use a browser. However you will have to take my word for the fact that the secondary search bar was taking up needed space, and the ability to combine previously visited webpage results with my current search query is a valuable interface improvement. I did not realize it supported OpenSearch, and by dissecting the XML file, I should be able to create a search string. I will post that if it works out.</p>
</div>
<div id="comment-9204-info" class="comment-info">
<span class="comment-age">(23 Nov '11, 12:25)</span> <span class="comment-user userinfo">ghoti</span>
</div>
</div>
<span id="21830"></span>
<div id="comment-21830" class="comment">
<div id="post-21830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This seems not to work (with firefox v19.0).</p>
</div>
<div id="comment-21830-info" class="comment-info">
<span class="comment-age">(25 Apr '13, 09:42)</span> <span class="comment-user userinfo">doak</span>
</div>
</div>
<span id="21846"></span>
<div id="comment-21846" class="comment">
<div id="post-21846-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still works for me (using Firefox 20.0, but I wouldn't expect that to make a difference).</p>
</div>
<div id="comment-21846-info" class="comment-info">
<span class="comment-age">(25 Apr '13, 12:56)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-9198" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9198-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9205"></span>

<div id="answer-container-9205" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9205-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-9205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Apparently the magic word was "query"</p>
<p><a href="http://www.openstreetmap.org/?query=%s">http://www.openstreetmap.org/?query=%s</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '11, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f947d945ccd9f9e8be5deab92abb41a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghoti&#39;s gravatar image" />
<p><span>ghoti</span><br />
<span class="score" title="116 reputation points">116</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghoti has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9205" class="comments-container">
<span id="21831"></span>
<div id="comment-21831" class="comment">
<div id="post-21831-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Worked. Thanks.</p>
</div>
<div id="comment-21831-info" class="comment-info">
<span class="comment-age">(25 Apr '13, 09:42)</span> <span class="comment-user userinfo">doak</span>
</div>
</div>
</div>
<div id="comment-tools-9205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9205-form-container" class="comment-form-container">
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

