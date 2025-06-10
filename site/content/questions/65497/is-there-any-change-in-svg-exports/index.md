+++
type = "question"
title = "Is there any change in SVG exports?"
description = '''Hi, was there any change in exporting SVG files for Inkscape?  I try it about 2 month ago and everything was normal - vectors etc. Now it is compact picture and can&#x27;t be ungrouped, so I can&#x27;t do anything with it. Thanks.'''
date = "2018-08-22T10:35:00Z"
lastmod = "2019-02-09T12:25:00Z"
weight = 65497
keywords = [ "svg", "vector", "inkscape" ]
aliases = [ "/questions/65497" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is there any change in SVG exports?](/questions/65497/is-there-any-change-in-svg-exports)

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
<span id="post-65497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, was there any change in exporting SVG files for Inkscape? I try it about 2 month ago and everything was normal - vectors etc. Now it is compact picture and can't be ungrouped, so I can't do anything with it. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-svg" rel="tag" title="see questions tagged &#39;svg&#39;">svg</span> <span class="post-tag tag-link-vector" rel="tag" title="see questions tagged &#39;vector&#39;">vector</span> <span class="post-tag tag-link-inkscape" rel="tag" title="see questions tagged &#39;inkscape&#39;">inkscape</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Aug '18, 10:35</strong></p>
<img src="https://secure.gravatar.com/avatar/bfe566a566f7e3382b8ad6d9aa832e61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martan1484&#39;s gravatar image" />
<p><span>martan1484</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martan1484 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '18, 21:57</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-65497" class="comments-container">
<span id="65498"></span>
<div id="comment-65498" class="comment">
<div id="post-65498-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain in a little bit more detail what your problem is? People won't be familiar with what you got last time or what you <em>were</em> able to do with it, and won't know what you are trying to do now.</p>
</div>
<div id="comment-65498-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 11:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65499"></span>
<div id="comment-65499" class="comment">
<div id="post-65499-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I suspect this is a result of an osm-carto style change which can’t be represented in SVG so forces rasterisation and output as an embedded bitmap.</p>
</div>
<div id="comment-65499-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 11:55)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="65500"></span>
<div id="comment-65500" class="comment">
<div id="post-65500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Richard, you are true, I think. Is there any possibility to change this and get SVG back in vectors instead of bitmap?</p>
</div>
<div id="comment-65500-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 12:26)</span> <span class="comment-user userinfo">martan1484</span>
</div>
</div>
<span id="65506"></span>
<div id="comment-65506" class="comment not_top_scorer">
<div id="post-65506-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which change could it be?</p>
<p>The problem is that there was no deployment of new OSM Carto version between v4.11.0 and v4.14.0:</p>
<p><a href="https://www.openstreetmap.org/user/kocio/diary/44222">https://www.openstreetmap.org/user/kocio/diary/44222</a></p>
<p><a href="https://www.openstreetmap.org/user/kocio/diary/44468">https://www.openstreetmap.org/user/kocio/diary/44468</a></p>
<p><a href="https://www.openstreetmap.org/user/kocio/diary/44713">https://www.openstreetmap.org/user/kocio/diary/44713</a></p>
</div>
<div id="comment-65506-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 20:19)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65507"></span>
<div id="comment-65507" class="comment not_top_scorer">
<div id="post-65507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11332/kocio">@kocio</a> Maybe a change to other software on the website? I know that some of the rendering chain has changed (e.g. to a version of osm2pgsql that doesn't tolerate old-style multipolygons) but I've no idea if anything behind the "export" button has changed.</p>
</div>
<div id="comment-65507-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 20:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="65508"></span>
<div id="comment-65508" class="comment">
<div id="post-65508-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Who knows - it's good to ask here probably:</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website/issues">https://github.com/openstreetmap/openstreetmap-website/issues</a></p>
</div>
<div id="comment-65508-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 20:56)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65511"></span>
<div id="comment-65511" class="comment not_top_scorer">
<div id="post-65511-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maybe introduction of comp-op? That seems to be a raster operation.</p>
</div>
<div id="comment-65511-info" class="comment-info">
<span class="comment-age">(22 Aug '18, 21:51)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="65522"></span>
<div id="comment-65522" class="comment not_top_scorer">
<div id="post-65522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Rather not, because comp-op has been introduced 4 years ago:</p>
<p><a href="https://github.com/gravitystorm/openstreetmap-carto/commit/7dfed686558830248ec986ad07411828bc103faf#diff-fa99f612b71d76a2335b976734997fbbR48">https://github.com/gravitystorm/openstreetmap-carto/commit/7dfed686558830248ec986ad07411828bc103faf#diff-fa99f612b71d76a2335b976734997fbbR48</a></p>
</div>
<div id="comment-65522-info" class="comment-info">
<span class="comment-age">(23 Aug '18, 02:33)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="65963"></span>
<div id="comment-65963" class="comment not_top_scorer">
<div id="post-65963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Has there been any progress/updates on the reasons for this change or whether this is going to change in the future?</p>
</div>
<div id="comment-65963-info" class="comment-info">
<span class="comment-age">(18 Sep '18, 13:32)</span> <span class="comment-user userinfo">strongy0484</span>
</div>
</div>
<span id="65969"></span>
<div id="comment-65969" class="comment not_top_scorer">
<div id="post-65969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I could not find any issue about this over at GitHub, so I opened one: <a href="https://github.com/openstreetmap/openstreetmap-website/issues/1998">https://github.com/openstreetmap/openstreetmap-website/issues/1998</a></p>
</div>
<div id="comment-65969-info" class="comment-info">
<span class="comment-age">(18 Sep '18, 19:18)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="66984"></span>
<div id="comment-66984" class="comment not_top_scorer">
<div id="post-66984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi everybody, Anybody has more information about this bug -&gt; SVG share generate PNG or BMP rendering ?<br />
Since the last post, nothing appends the problem seems to be unsolved. I'm not developer, so I really don't understand all exchanges about this issue.<br />
If anybody knows more about it and if anybody can explain it in common language, please let us know ;-)<br />
Thanks in advance and have a good day guys !!!</p>
</div>
<div id="comment-66984-info" class="comment-info">
<span class="comment-age">(29 Nov '18, 10:25)</span> <span class="comment-user userinfo">gAte1983</span>
</div>
</div>
<span id="66987"></span>
<div id="comment-66987" class="comment">
<div id="post-66987-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15976/gate1983">@gate1983</a> the short answer is "no" - I don't believe that anything has changed. The issue <a href="https://github.com/mapnik/mapnik/issues/3749">https://github.com/mapnik/mapnik/issues/3749</a> is closed, but (to some commenters there, and you) still an issue.</p>
</div>
<div id="comment-66987-info" class="comment-info">
<span class="comment-age">(29 Nov '18, 11:16)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="67312"></span>
<div id="comment-67312" class="comment not_top_scorer">
<div id="post-67312-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>previous question about the same: <a href="https://help.openstreetmap.org/questions/58913/mapnik-svg-output-not-working">https://help.openstreetmap.org/questions/58913/mapnik-svg-output-not-working</a></p>
</div>
<div id="comment-67312-info" class="comment-info">
<span class="comment-age">(21 Dec '18, 22:04)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65497" class="comment-tools">
<span class="comments-showing"> showing 5 of 13 </span> <a href="#" class="show-all-comments-link">show 8 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-65497-form-container" class="comment-form-container">
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

<span id="67940"></span>

<div id="answer-container-67940" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67940-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-67940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This bug seems to be fixed now. It looks like a Mapnik problem, but there's also a workaround deployed in the export code on the OSM.org website which works immediately. See more details in <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/3653">https://github.com/gravitystorm/openstreetmap-carto/issues/3653</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '19, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span> </br></br></p>
</div>
</div>
<div id="comments-container-67940" class="comments-container">
<span id="67947"></span>
<div id="comment-67947" class="comment">
<div id="post-67947-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: Thanks for your follow-up on this! I hope the OP <a href="https://help.openstreetmap.org/users/15561/martan1484">@martan1484</a> does not mind, I have "accepted" this as answer for their question.</p>
</div>
<div id="comment-67947-info" class="comment-info">
<span class="comment-age">(09 Feb '19, 12:25)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67940-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67314"></span>

<div id="answer-container-67314" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67314-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67314-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67314-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems to be (and stays) broken (see comments). Use another way to get a <a href="https://wiki.openstreetmap.org/wiki/SVG">SVG map based on OSM data</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '18, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span> </br></p>
</div>
</div>
<div id="comments-container-67314" class="comments-container">
&#10;</div>
<div id="comment-tools-67314" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67314-form-container" class="comment-form-container">
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

