+++
type = "question"
title = "[closed] Problem Starting Firefox With OSM URL Containing Ampersand"
description = '''I&#x27;m working on some software that does its calcs. and then starts up a new Firefox browser window passing the OSM URL and the relevant Lat. and Lon. parameters, e.g. http://www.openstreetmap.org/?lat=52.1917&amp;amp;lon=-1.7073&amp;amp;zoom=12 However nothing from the first ampersand onwards appears in the ...'''
date = "2012-10-25T16:38:00Z"
lastmod = "2012-10-25T16:56:00Z"
weight = 17184
keywords = [ "url", "ampersand", "parameter", "firefox" ]
aliases = [ "/questions/17184" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Problem Starting Firefox With OSM URL Containing Ampersand](/questions/17184/problem-starting-firefox-with-osm-url-containing-ampersand)

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
<span id="post-17184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm working on some software that does its calcs. and then starts up a new Firefox browser window passing the OSM URL and the relevant Lat. and Lon. parameters, e.g. <a href="http://www.openstreetmap.org/?lat=52.1917&amp;lon=-1.7073&amp;zoom=12">http://www.openstreetmap.org/?lat=52.1917&amp;lon=-1.7073&amp;zoom=12</a></p>
<p>However nothing from the first ampersand onwards appears in the Firefox address bar, and Firefox just displays the last OSM map view viewed in Firefox, regardless of the actual Lat. in the address bar. Have tried executing the full command (i.e. that issued by my software) from the command prompt in the "DOS window", e.g... "C:\Program Files\Mozilla Firefox\firefox.exe" -new-tab <a href="http://www.openstreetmap.org/?lat=52.1917&amp;lon=-1.7073&amp;zoom=12">http://www.openstreetmap.org/?lat=52.1917&amp;lon=-1.7073&amp;zoom=12</a> and the error messages I get are 'lon' is not recognized as an internal or external command, operable program or batch file. 'zoom' is not recognized as an internal or external command, operable program or batch file.</p>
<p>So it seems to me that WinXP is doing some parsing of the parameter string being passed to Firefox and only actually passing the "lat" parameter to Firefox.</p>
<p>I tried escaping the ampersands with %26 and the whole parameter string then gets through to Firefox but the OSM server (or Firefox?) seems not to recognise the escaped ampersands, thereby displaying the last map shown. I've tried with a semicolon as an alternative delimiter (which, I believe, is supposed to be a valid delimiter) and also the comma, but they just display the last map shown as described above.</p>
<p>Regular URLs without the ampersand, e.g. a tile URL (<a href="http://tile.openstreetmap.org/12/2028/1349.png">http://tile.openstreetmap.org/12/2028/1349.png</a>), work fine.</p>
<p>It seems the required ampersand in the query parameter is tripping me up via WinXP! Any ideas on a resolution? Ta!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-ampersand" rel="tag" title="see questions tagged &#39;ampersand&#39;">ampersand</span> <span class="post-tag tag-link-parameter" rel="tag" title="see questions tagged &#39;parameter&#39;">parameter</span> <span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '12, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/956d6fda0f51e8001832540fa2c716a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vagabond&#39;s gravatar image" />
<p><span>vagabond</span><br />
<span class="score" title="195 reputation points">195</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vagabond has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>25 Oct '12, 16:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-17184" class="comments-container">
&#10;</div>
<div id="comment-tools-17184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17184-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by SomeoneElse 25 Oct '12, 16:57

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17185"></span>

<div id="answer-container-17185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17185-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not that it's anything to do with OSM, but you need to put quotes around the address like you did around the program:</p>
<pre><code>&quot;C:\Program Files\Mozilla Firefox\firefox.exe&quot; -new-tab &quot;http://www.openstreetmap.org/?lat=52.1917&amp;lon=-1.7073&amp;zoom=12&quot;</code></pre>
<p>If you don't do that Windows will try and parse the command line rather than just passing it to Firefox.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '12, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17185" class="comments-container">
&#10;</div>
<div id="comment-tools-17185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17185-form-container" class="comment-form-container">
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

