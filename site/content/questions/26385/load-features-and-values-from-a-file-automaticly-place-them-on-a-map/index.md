+++
type = "question"
title = "[closed] load features and values from a file automaticly place them on a map"
description = '''Hi I&#x27;d like to be able to define my own place names (features) and categories (values). use custom calcs/traces (feature/value) and automaticly place them on a map by loading a file. On the map, each calc/trace (feature/value) would be a colored dot. In the file the first column would be the RGB col...'''
date = "2013-09-16T16:04:00Z"
lastmod = "2013-09-16T16:41:00Z"
weight = 26385
keywords = [ "source" ]
aliases = [ "/questions/26385" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] load features and values from a file automaticly place them on a map](/questions/26385/load-features-and-values-from-a-file-automaticly-place-them-on-a-map)

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
<span id="post-26385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26385-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'd like to be able to define my own place names (features) and categories (values).</p>
<p>use custom calcs/traces (feature/value) and automaticly place them on a map by loading a file. On the map, each calc/trace (feature/value) would be a colored dot. In the file the first column would be the RGB color code (HTML format #RRGGBB) (Ex. FF0000, 0000FF) the second column would be the place type (Ex. 0000, FFFF) and the following columns (on the same line) would be the complet address inside single qoutes.</p>
<p>in this example: 0000 corresponding to 'restaurant' FFFF corresponding to 'gas station' FF0000 corresponding to red in HTML 0000FF corresponding to blue in HTML</p>
<p>Ex. FF0000 0000 '1234 Main st. Smalltown CA. U.S.A.' 0000FF FFFF '4000 5nd st. Smalltown CA. U.S.A.'</p>
<p>This would place 1 red and 1 blue dots in the map at those 2 addresse locations and zoom in if necessary. The zoom parameters would be user defined.</p>
<p>Each line in the file (seperated by \n \r \n\r for UNIX/MAC/Windows resp.) corresponding to a dot on the map. There can an an infinit (modulo OS/device limits) number of lines in a file (dots on the map). If 2 or more dots point at the same addresse then if they are the same color then place the number of dots inside the red dot on the map. I use the color of the dot (in this case red) when 2 or more dots point at the same addresse and are not different. Ex. if '1234 Main st. Smalltown CA. U.S.A.' has 2 restorants then '2' would appear on the map at '1234 Main st. Smalltown CA. U.S.A.' within a red dot.Clicking on it would expand to 2 red dots.</p>
<p>If they are the not same color then place the number of dots inside alternating color the dot on the map. I use the alternating color dot when 2 or more dots point at the same addresse and are different. Ex. if '1234 Main st. Smalltown CA. U.S.A.' has 1 restorant and a gas station then '2' would appear on the map at '1234 Main st. Smalltown CA. U.S.A.' within a alternating color dot. In this case red and blue.In this case the above file contents would be: FF0000 0000 '1234 Main st. Smalltown CA. U.S.A.' 0000FF FFFF '1234 Main st. Smalltown CA. U.S.A.' Clicking on it would expand to 1 red and 1 blue dot.</p>
<p>The alternating color would be those of the correcponding items.In this case red (FF0000) and blue (0000FF). The alternating time is user defined.</p>
<p>The exact rendering of those dot would be depandant on the number of dots and location within the map taking into account the available screen space.It is unspecified weather they are from left to right,top to bottom, ect...</p>
<p>Thx :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '13, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/e2905869cc2064b47c77d62d0ef48b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc0&#39;s gravatar image" />
<p><span>Marc0</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc0 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>16 Sep '13, 16:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-26385" class="comments-container">
<span id="26394"></span>
<div id="comment-26394" class="comment">
<div id="post-26394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is a question-and-answer site. If you would like to make suggestions as to how openstreetmap.org can function better, please use <a href="http://trac.openstreetmap.org/">http://trac.openstreetmap.org/</a> , or better still get involved and contribute code. Thanks!</p>
</div>
<div id="comment-26394-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 16:41)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-26385" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26385-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not a question" by Richard 16 Sep '13, 16:41

</div>

</div>

</div>

