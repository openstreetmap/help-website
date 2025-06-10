+++
type = "question"
title = "Tile Server, some tiles randomly not loading with error: ERR_CERT_DATE_INVALID"
description = '''My tile server is randomly not loading certain tiles, with the error message (failed) net::ERR_CERT_DATE_INVALID. Here is a picture that shows that the issue. I tried the site on multiple devices and browsers, and the issue is the same. So something is happening server-side on the tile server. This ...'''
date = "2020-08-02T06:34:00Z"
lastmod = "2020-08-02T09:17:00Z"
weight = 75981
keywords = [ "tile", "tileserver" ]
aliases = [ "/questions/75981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tile Server, some tiles randomly not loading with error: ERR_CERT_DATE_INVALID](/questions/75981/tile-server-some-tiles-randomly-not-loading-with-error-err_cert_date_invalid)

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
<span id="post-75981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75981-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My tile server is randomly not loading certain tiles, with the error message (failed) net::ERR_CERT_DATE_INVALID.</p>
<p><a href="https://i.gyazo.com/9c90a5b210f6473aecd0cad86aaebd28.jpg">Here is a picture</a> that shows that the issue.</p>
<p>I tried the site on multiple devices and browsers, and the issue is the same. So something is happening server-side on the tile server.</p>
<p>This issue happens sporadically. In fact, the same tiles that didn't load initially would load just fine after I refresh the page.</p>
<p>But it is definitely very annoying to have to refresh the page constantly because certain tiles are not loading.</p>
<p>Anyone know why this problem is happening? It happens randomly and I haven't been able to pinpoint it so far, apart from the fact that the problem is happening in the 158th line in TileLayer.js, which is the following line:</p>
<pre><code>tile.src = this.getTileUrl(coords);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tile" rel="tag" title="see questions tagged &#39;tile&#39;">tile</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '20, 06:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b1e3fbb6f31c5e0144e7b18fcd7d5d33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valachio&#39;s gravatar image" />
<p><span>valachio</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valachio has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '20, 06:35</strong> </span></p>
</div>
</div>
<div id="comments-container-75981" class="comments-container">
&#10;</div>
<div id="comment-tools-75981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75981-form-container" class="comment-form-container">
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

<span id="75982"></span>

<div id="answer-container-75982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75982-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is probably due to time issues on your server or the client, check that both are set correctly and are synchronized, for example with NTP. It could very well be that the time offsets are just so that things some time fails some time not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '20, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-75982" class="comments-container">
&#10;</div>
<div id="comment-tools-75982" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75982-form-container" class="comment-form-container">
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

