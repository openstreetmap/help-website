+++
type = "question"
title = "Mapnik does not show &quot;shop:electronics&quot;"
description = '''Hi, I found out that Mapnik does not show shops marked with &quot;electronics&quot; and in Potlatch you cannot select this shop type. In Germany there are two big electroincs chains (&quot;Saturn&quot; and &quot;Media Markt&quot;) that are already mapped as &quot;shop:electronics&quot; and they won&#x27;t show up. Is there a way to add this to...'''
date = "2012-11-15T14:31:00Z"
lastmod = "2012-11-19T11:33:00Z"
weight = 17729
keywords = [ "shop", "mapnik" ]
aliases = [ "/questions/17729" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik does not show "shop:electronics"](/questions/17729/mapnik-does-not-show-shopelectronics)

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
<span id="post-17729-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17729-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17729-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I found out that Mapnik does not show shops marked with "electronics" and in Potlatch you cannot select this shop type.</p>
<p>In Germany there are two big electroincs chains ("Saturn" and "Media Markt") that are already mapped as "shop:electronics" and they won't show up. Is there a way to add this to the render engine?</p>
<p>Thanks in advance! (EDIT: Do not mean Osmrenderer but Mapnik)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shop" rel="tag" title="see questions tagged &#39;shop&#39;">shop</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '12, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/670e6df1e60fc46ad21fd4b62f84fa6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sokke90&#39;s gravatar image" />
<p><span>sokke90</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sokke90 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '12, 14:46</strong> </span></p>
</div>
</div>
<div id="comments-container-17729" class="comments-container">
&#10;</div>
<div id="comment-tools-17729" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17729-form-container" class="comment-form-container">
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

<span id="17735"></span>

<div id="answer-container-17735" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17735-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="https://help.openstreetmap.org/users/87/pieren">Pieren</a> said, "why is XYZ not rendered on the main map" is a question that is asked quite frequently. <a href="https://help.openstreetmap.org/questions/17642/why-do-some-shops-not-appear-on-the-default-mapnik-map">This</a> is a question from someone from Sweden about "shop=alcohol". <a href="http://help.openstreetmap.org/questions/17642/why-do-some-shops-not-appear-on-the-default-mapnik-map/17643">Frederik's answer</a> explains where the code is and what the mechanism currently is for requesting changes to it.</p>
<p>However, it's worth expanding a little on that. <a href="http://lists.openstreetmap.org/pipermail/dev/2012-November/026125.html">This mailing list thread</a> discusses the current problems with main map style and how easy it is (or not) to contribute to it. In some cases the problem is that the data currently isn't in the rendering database so adding it requires more than just a style file change (I don't think that that's the case with "shop", though)</p>
<p>With regard to the second part of your question "in Potlatch you cannot select this shop type", have a look at <a href="https://help.openstreetmap.org/questions/4672/how-to-request-an-icon-be-added-in-potlatch2-for-barrierentrance">this previous question</a>. The procedure's similar to the main map style - log a bug in <a href="http://trac.openstreetmap.org/">trac</a> using your normal OSM login, assign it to the correct area (in this case "potlatch2"), and offer whatever help (icons etc.) that you can. In the case of Potlatch new trac entries are forwarded to a <a href="http://lists.openstreetmap.org/pipermail/potlatch-dev/">mailing list</a> where they can be discussed further.</p>
<p>In Potlatch you can, of course, always select "advanced" mode and add whatever tags you like.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17735" class="comments-container">
&#10;</div>
<div id="comment-tools-17735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17735-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17801"></span>

<div id="answer-container-17801" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17801-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17801-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17801-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Additionnaly to other answer about OSM's mapnik policy, you can use other tools for viewing the wanted data. For example, you can use this xapiviewer to see <a href="http://osm.dumoulin63.net/xapiviewer/?zoom=15&amp;lat=52.51788&amp;lon=13.39604&amp;layers=B0T&amp;icon=icons%2Fshopping_computer.n.32.png&amp;request=shop%3Delectronics">such shops in Berlin</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '12, 11:33</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-17801" class="comments-container">
&#10;</div>
<div id="comment-tools-17801" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17801-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17731"></span>

<div id="answer-container-17731" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17731-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please use the 'search' function to find previous questions about the same topic. E.g. <a href="https://help.openstreetmap.org/questions/1107/can-i-influence-what-gets-rendered-in-the-main-mapnik-layer">https://help.openstreetmap.org/questions/1107/can-i-influence-what-gets-rendered-in-the-main-mapnik-layer</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '12, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17731" class="comments-container">
<span id="17733"></span>
<div id="comment-17733" class="comment">
<div id="post-17733-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That was a good answer in its time but has been rather overtaken by events (Osmarender no longer exists, for example).</p>
</div>
<div id="comment-17733-info" class="comment-info">
<span class="comment-age">(15 Nov '12, 16:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17731-form-container" class="comment-form-container">
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

