+++
type = "question"
title = "not understand function"
description = '''Hello everybody, I don&#x27;t get the function. I have registered to OSM. I was directed here from Wikipedia. I&#x27;ve got a direct link: https://www.openstreetmap.org/?relation=103398 But when I klick, I can see nothing. Whats wrong? My intent is to get a map file for the Donauradweg from Passau to Wien. I w...'''
date = "2012-08-13T10:55:00Z"
lastmod = "2012-08-13T12:33:00Z"
weight = 15006
keywords = [ "download", "file", "donauradweg", "mapfile" ]
aliases = [ "/questions/15006" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [not understand function](/questions/15006/not-understand-function)

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
<span id="post-15006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15006-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody, I don't get the function. I have registered to OSM. I was directed here from Wikipedia. I've got a direct link: <a href="https://www.openstreetmap.org/?relation=103398">https://www.openstreetmap.org/?relation=103398</a> But when I klick, I can see nothing. Whats wrong? My intent is to get a map file for the Donauradweg from Passau to Wien.</p>
<p>I want to import the file into a smartphone app or navigational tools, so I will probably need a GPX or KML file.</p>
<p>Would anybody mind giving me some basics or in the best a solution for my issue? Thanks in forehand, Thomas</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-donauradweg" rel="tag" title="see questions tagged &#39;donauradweg&#39;">donauradweg</span> <span class="post-tag tag-link-mapfile" rel="tag" title="see questions tagged &#39;mapfile&#39;">mapfile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '12, 10:55</strong></p>
<img src="https://secure.gravatar.com/avatar/44a19769a6db824bfddbfbbfbe3f4511?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toohoo&#39;s gravatar image" />
<p><span>toohoo</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toohoo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '12, 11:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-15006" class="comments-container">
&#10;</div>
<div id="comment-tools-15006" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15006-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="15018"></span>

<div id="answer-container-15018" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15018-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-15018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To obtain a GPX:</p>
<p>Please start <a href="http://josm.openstreetmap.de/">JOSM</a>. Choose there "File &gt; Open Adress ..." and enter into the address textline</p>
<pre><code>http://overpass-api.de/api/interpreter?data=(rel(103398);&gt;&gt;;);out+meta;</code></pre>
<p>This downloads all the objects that belong to relation 103398. Now you can view the relation. To get a GPX, go to "File &gt; Save As ..." and choose there as file type GPX.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '12, 12:33</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-15018" class="comments-container">
&#10;</div>
<div id="comment-tools-15018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15018-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15011"></span>

<div id="answer-container-15011" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15011-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15011-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15011-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To visualise it, try having a look at "DCP" on Lonvia's cycle map <a href="http://cycling.lonvia.de/de/?zoom=8&amp;lat=48.37177&amp;lon=14.3771">here</a>. When you say you want a "map file" what format do you want it in?</p>
<p>The link that you were given was a "show a relation on a large map" one and doesn't seem to be working for that relation, possibly because it <a href="https://www.openstreetmap.org/browse/relation/103398">consists only of smaller relations</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '12, 11:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-15011" class="comments-container">
&#10;</div>
<div id="comment-tools-15011" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15011-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15013"></span>

<div id="answer-container-15013" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15013-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15013-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15013-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason you don't understand how it works is that you are not using it in the "normal" way. OSM doesn't have an interface for downloading and exporting individual objects like this; you will need third-party software to do the export for you. One possible solution might be</p>
<p><a href="http://mr-unseld.de/?q=de/node/170">http://mr-unseld.de/?q=de/node/170</a></p>
<p>although this might not work with the kind of cascading relation you have here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '12, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-15013" class="comments-container">
<span id="15014"></span>
<div id="comment-15014" class="comment">
<div id="post-15014-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Frederik, just to understand you right. There would be no way to get a navigational route out of OSM which I can use vor navigation my bicycle? Okay, I will do this route in August. What will it need to record my route and share it on OSM? Thanks in forehand, Thomas</p>
</div>
<div id="comment-15014-info" class="comment-info">
<span class="comment-age">(13 Aug '12, 12:10)</span> <span class="comment-user userinfo">toohoo</span>
</div>
</div>
<span id="15015"></span>
<div id="comment-15015" class="comment">
<div id="post-15015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The route itself is in OSM, but OSM does not offer an interface where you can download it directly into your device. There are several navigation applications based on OSM and you can also load OSM data into a Garmin device; in each case, the way you are interested in will very likely be present in the data. It's just that OpenStreetMap does not have a web interface where you can say "please download this one cycle route into my device". - Try www.bikemap.net which is made specifically for sharing cycle routes.</p>
</div>
<div id="comment-15015-info" class="comment-info">
<span class="comment-age">(13 Aug '12, 12:23)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-15013" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15013-form-container" class="comment-form-container">
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

