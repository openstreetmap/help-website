+++
type = "question"
title = "getosm.py doesn&#x27;t work"
description = '''When I try to use the getosm.py script, it shows the message : &quot;At least one of &#x27;bbox&#x27; and &#x27;area&#x27; and &#x27;polygon&#x27; has to be set&quot; and I don&#x27;t know why. I&#x27;m using that because I want to get a big area.'''
date = "2017-07-09T03:45:00Z"
lastmod = "2017-07-09T07:56:00Z"
weight = 56967
keywords = [ "extract", "osm" ]
aliases = [ "/questions/56967" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [getosm.py doesn't work](/questions/56967/getosmpy-doesnt-work)

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
<span id="post-56967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to use the getosm.py script, it shows the message : "At least one of 'bbox' and 'area' and 'polygon' has to be set" and I don't know why. I'm using that because I want to get a big area.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '17, 03:45</strong></p>
<img src="https://secure.gravatar.com/avatar/be65e74084620c00e4c3260ddd85db47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andressa_dps&#39;s gravatar image" />
<p><span>Andressa_dps</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andressa_dps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56967" class="comments-container">
<span id="56968"></span>
<div id="comment-56968" class="comment">
<div id="post-56968-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you show us the exact command that you type? It seems like you are not specifying a required argument</p>
</div>
<div id="comment-56968-info" class="comment-info">
<span class="comment-age">(09 Jul '17, 07:34)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-56967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56967-form-container" class="comment-form-container">
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

<span id="56969"></span>

<div id="answer-container-56969" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56969-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While escada is certainly correct, it doesn't really matter: you will not be successful in directly downloading a "large" area and you shouldn't try to work around the size limitations.</p>
<p>You either need to download a planet dump and extract the area in question, or use pre-defined extracts or an extract service: <a href="http://planet.openstreetmap.org/">http://planet.openstreetmap.org/</a> has links to some of the providers.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '17, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '17, 08:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-56969" class="comments-container">
&#10;</div>
<div id="comment-tools-56969" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56969-form-container" class="comment-form-container">
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

