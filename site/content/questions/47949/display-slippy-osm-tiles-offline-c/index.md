+++
type = "question"
title = "Display slippy osm tiles offline c++"
description = '''Hi, I have a problem: I need to display slippy tiles (png images) offline and work with these tiles (zooming, moving etc.) in my c++ application, please help me how can I do it? Thank you!'''
date = "2016-02-05T11:51:00Z"
lastmod = "2017-01-03T10:47:00Z"
weight = 47949
keywords = [ "tiles", "slippy", "c++", "offline" ]
aliases = [ "/questions/47949" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Display slippy osm tiles offline c++](/questions/47949/display-slippy-osm-tiles-offline-c)

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
<span id="post-47949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47949-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have a problem: I need to display slippy tiles (png images) offline and work with these tiles (zooming, moving etc.) in my c++ application, please help me how can I do it? Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-slippy" rel="tag" title="see questions tagged &#39;slippy&#39;">slippy</span> <span class="post-tag tag-link-c++" rel="tag" title="see questions tagged &#39;c++&#39;">c++</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 11:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ef834deb999befeea6927ffb753ef9de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DmitriyUa&#39;s gravatar image" />
<p><span>DmitriyUa</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DmitriyUa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Feb '16, 12:47</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-47949" class="comments-container">
<span id="47950"></span>
<div id="comment-47950" class="comment">
<div id="post-47950-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>crosspost: <a href="https://gis.stackexchange.com/questions/178506/osm-tiles-offline-display-using-c">https://gis.stackexchange.com/questions/178506/osm-tiles-offline-display-using-c</a></p>
</div>
<div id="comment-47950-info" class="comment-info">
<span class="comment-age">(05 Feb '16, 11:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47949-form-container" class="comment-form-container">
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

<span id="47951"></span>

<div id="answer-container-47951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47951-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Perhaps <a href="http://www.medieninf.de/qmapcontrol/">http://www.medieninf.de/qmapcontrol/</a> or <a href="https://wiki.gnome.org/Projects/libchamplain">https://wiki.gnome.org/Projects/libchamplain</a> are options for you. Also see the <a href="http://wiki.openstreetmap.org/wiki/Frameworks">Frameworks page on the wiki.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Feb '16, 12:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47951" class="comments-container">
&#10;</div>
<div id="comment-tools-47951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47951-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53820"></span>

<div id="answer-container-53820" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53820-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try to include Gecko library in your application to have a web browser, and browse a web map application, you make, using Openlayers or LeafletJS...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jan '17, 10:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1638dfb4bbd6c90cefa57e6d847354c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="offygis&#39;s gravatar image" />
<p><span>offygis</span><br />
<span class="score" title="25 reputation points">25</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="offygis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-53820" class="comments-container">
&#10;</div>
<div id="comment-tools-53820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53820-form-container" class="comment-form-container">
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

