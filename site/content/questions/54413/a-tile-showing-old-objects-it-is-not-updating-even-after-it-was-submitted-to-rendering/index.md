+++
type = "question"
title = "A tile showing old objects... it is not updating even after it was submitted to rendering."
description = '''Hi, I&#x27;ve duplicated some objects by mistake, and then I reverted my mistake, but the tile showing it remains even though days have passed.  I&#x27;ve submitted the tile for rendering by adding /dirty to its url, but that doesn&#x27;t seem to work. The tile&#x27;s URL is https://a.tile.openstreetmap.org/17/72908/42...'''
date = "2017-02-01T20:56:00Z"
lastmod = "2017-02-02T12:36:00Z"
weight = 54413
keywords = [ "rendering", "tiles", "mapnik" ]
aliases = [ "/questions/54413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [A tile showing old objects... it is not updating even after it was submitted to rendering.](/questions/54413/a-tile-showing-old-objects-it-is-not-updating-even-after-it-was-submitted-to-rendering)

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
<span id="post-54413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54413-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I've duplicated some objects by mistake, and then I reverted my mistake, but the tile showing it remains even though days have passed.</p>
<p>I've submitted the tile for rendering by adding /dirty to its url, but that doesn't seem to work. The tile's URL is <a href="https://a.tile.openstreetmap.org/17/72908/42319.png,">https://a.tile.openstreetmap.org/17/72908/42319.png,</a> it is visible only at one zoom level. The location affected is here: <a href="https://www.openstreetmap.org/#map=17/53.61837/20.25000">https://www.openstreetmap.org/#map=17/53.61837/20.25000</a></p>
<p>Please let me know if I can do anything else to fix this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '17, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/18d340943db47a7e99da02b235325082?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LukaszME&#39;s gravatar image" />
<p><span>LukaszME</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LukaszME has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54413" class="comments-container">
&#10;</div>
<div id="comment-tools-54413" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54413-form-container" class="comment-form-container">
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

<span id="54414"></span>

<div id="answer-container-54414" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OK, I'm going to reply to my own question as I found a solution.</p>
<p>The tile's address starts with a.tile.openstreetmap.org. After I changed the address and I opened <a href="http://b.tile.openstreetmap.org/17/72908/42319.png/dirty">http://b.tile.openstreetmap.org/17/72908/42319.png/dirty</a> and then <a href="http://b.tile.openstreetmap.org/17/72908/42319.png/ditry">http://b.tile.openstreetmap.org/17/72908/42319.png/ditry</a> the tile finally was rendered.</p>
<p>I think there is an issue with that server hiding under a. Once I submitted the tile though one of other servers it started working.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '17, 21:05</strong></p>
<img src="https://secure.gravatar.com/avatar/18d340943db47a7e99da02b235325082?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LukaszME&#39;s gravatar image" />
<p><span>LukaszME</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LukaszME has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54414" class="comments-container">
<span id="54420"></span>
<div id="comment-54420" class="comment">
<div id="post-54420-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Flagging a tile as "dirty" doesn't immediately trigger a re-rendering. Depending on the zoom level and the current tile server load this can take quite a while.</p>
</div>
<div id="comment-54420-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 08:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54428"></span>
<div id="comment-54428" class="comment">
<div id="post-54428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hmm, yes I saw this mentioned in few places, but how long is "a while"? I waited 3 days and the old tile was still there. Also when queried with the /status the server was claiming the tile is not dirty but clean despite it being submitted for rendering...</p>
<p>It looks like a bug.</p>
</div>
<div id="comment-54428-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 12:31)</span> <span class="comment-user userinfo">LukaszME</span>
</div>
</div>
<span id="54429"></span>
<div id="comment-54429" class="comment">
<div id="post-54429-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"a while" depends on how busy the server is. If you absolutely want to have up to date tiles and not wait for OSM's, I'd suggest running your own tile server.</p>
</div>
<div id="comment-54429-info" class="comment-info">
<span class="comment-age">(02 Feb '17, 12:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54414-form-container" class="comment-form-container">
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

