+++
type = "question"
title = "Pragmatic, single-level indoor paths"
description = '''I&#x27;m adding more details to some single-level malls (shop names and locations, mainly), and I&#x27;d like there to be paths showing the corridors and entrances/exits. I&#x27;d like them to show on most renderers, such as OSMAnd, standard map layer on the website, etc. However, the indoor=corridor tags are not ...'''
date = "2017-12-06T07:57:00Z"
lastmod = "2017-12-07T14:10:00Z"
weight = 61025
keywords = [ "indoor" ]
aliases = [ "/questions/61025" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Pragmatic, single-level indoor paths](/questions/61025/pragmatic-single-level-indoor-paths)

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
<span id="post-61025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61025-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm adding more details to some single-level malls (shop names and locations, mainly), and I'd like there to be paths showing the corridors and entrances/exits. I'd like them to show on most renderers, such as OSMAnd, standard map layer on the website, etc. However, the <code>indoor=corridor</code> tags are not currently shown, and if I try <code>highway=pedestrian</code>, for instance, it complains about lack of names with warnings.</p>
<p>What would be the simplest, most pragmatic way to get useful results (showing paths inside the mall, just to give a general idea for people having never been there) without requiring special renderers?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '17, 07:57</strong></p>
<img src="https://secure.gravatar.com/avatar/395b52b769f88f777174aeadaaf4be12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voyageant&#39;s gravatar image" />
<p><span>voyageant</span><br />
<span class="score" title="181 reputation points">181</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voyageant has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61025" class="comments-container">
<span id="61034"></span>
<div id="comment-61034" class="comment">
<div id="post-61034-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>highway=pedestrian is essentially short for "pedestrianized road", so it's very unlikely to be accurate for an indoor mall.</p>
</div>
<div id="comment-61034-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 16:57)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-61025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61025-form-container" class="comment-form-container">
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

<span id="61043"></span>

<div id="answer-container-61043" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61043-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61043-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61043-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voyageant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please use the tags documented in <strong><a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">Simple Indoor Tagging</a></strong>, such as <strong>indoor=corridor</strong>. It's significantly streamlined compared with previous iterations of indoor tagging (which made heavy use of relations, for example) and it's supported in indoor renderers like <a href="https://openlevelup.net/">OpenLevelUp</a> (<a href="https://wiki.openstreetmap.org/wiki/OpenLevelUp">wiki</a>).</p>
<p>Using a consistent tagging standard gives the best results for the most people, and is therefore the most pragmatic solution – if you consider the long term effects rather than just the immediate benefits.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 18:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-61043" class="comments-container">
<span id="61055"></span>
<div id="comment-61055" class="comment">
<div id="post-61055-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do believe the examples discussed here are a halfway stage between standard &amp; indoor tagging. There are multiple places where significant parts of the public highway network for pedestrians passes through covered spaces, and at a minimum fulfil the functional aspects of highway=footway.</p>
<p>Please show a router which will standardly include such covered routes mapped as indoor=corridor. Then I might accept that this is a pragmatic solution which the OP asked for.</p>
<p>Lastly, the usage I describe long pre-dates indoor tagging schemes, and pragmatic solutions must take such factors in account.</p>
</div>
<div id="comment-61055-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 21:21)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="61056"></span>
<div id="comment-61056" class="comment">
<div id="post-61056-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Would it be incorrect and/or counterproductive to add both tags, <code>highway=footway</code> <strong>and</strong> <code>indoor=corridor</code>? The idea being that the former will be removed once the latter is displayed on standard layers/routers?</p>
</div>
<div id="comment-61056-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 21:38)</span> <span class="comment-user userinfo">voyageant</span>
</div>
</div>
<span id="61058"></span>
<div id="comment-61058" class="comment">
<div id="post-61058-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14436/voyageant"></a><a href="https://help.openstreetmap.org/users/14436/voyageant">@voyageant</a>: This could be a compromise, but keep in mind that indoor=corridor is intended for area-based mapping. (Which, if you weren't aware of this before, probably makes the tag look even less pragmatic. :P) So unless you're going to use highway=footway on areas, too, the tags will need to go on separate geometries.</p>
<p><a href="https://help.openstreetmap.org/users/647/sk53"></a><a href="https://help.openstreetmap.org/users/647/sk53">@SK53</a> OSMAnd is <a href="https://taginfo.openstreetmap.org/tags/indoor=corridor#projects">listed</a> as supporting indoor=corridor, although I'm not sure if that's actually correct. To be honest, I've been deliberately glossing over the "must show up on standard map and OSMAnd" requirement here because I feel that it's against community norms to base the decision on those factors – <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">tagging for the renderer</a> and all that. Of course, your answer argues that indoor highway=footway can be a decent choice to represent reality, and not <em>just</em> an attempt to get things rendered. I'm not convinced that it's actually a good choice here, but I'll admit that using is not inherently incorrect.</p>
</div>
<div id="comment-61058-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 22:36)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
<span id="61059"></span>
<div id="comment-61059" class="comment">
<div id="post-61059-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is "indoor=corridor" a solution to the same problem? <a href="https://wiki.openstreetmap.org/wiki/Key:indoor">https://wiki.openstreetmap.org/wiki/Key:indoor</a> links to <a href="https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging">https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging</a> which says "corridors ... are mapped as ... areas"; so it's not actually doing the same job on the map as e.g. highway=footway (though this doesn't of course make highway=footway "correct" or indoor=corridor "incorrect", just different).</p>
<p>(edit: oops - 2 comments composed at the same time; Tordanik addresses some of this above)</p>
</div>
<div id="comment-61059-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 22:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61068"></span>
<div id="comment-61068" class="comment">
<div id="post-61068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14/tordanik">@Tordanik</a>: just looked at my furtive attempts at indoor mapping &amp; see I did use corridor as area. I'm not particularly wild about some of these usages either, but having a representation which gives wildly misleading impressions of pedestrian network connectivity doesn't help either. On the entirely pragmatic level I want accurate timings of how long it will take me to get to the tram stop &amp; the route takes me through the middle of a hospital. :-) Perhaps we can consider this further on the wiki.</p>
</div>
<div id="comment-61068-info" class="comment-info">
<span class="comment-age">(07 Dec '17, 14:10)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61043" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61043-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61029"></span>

<div id="answer-container-61029" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61029-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-61029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The use of <strong>highway=footway</strong> for routes inside shopping centres and malls is widespread.</p>
<p>These are often really part of the public realm; and most should be treated as such, even if closed at night. In some cities in North America (Edmonton, Minneapolis come to mind) many pedestrian routes, such as the Minneapolis Skyway, across the city centre (downtown/CBD) are totally enclosed so that much of the main shopping area is of this form.</p>
<p>Additional tags which can be used are tunnel=building_passage and indoor=yes. Opening hours tags could be added to routes which are not open 24/7.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '17, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-61029" class="comments-container">
<span id="61044"></span>
<div id="comment-61044" class="comment">
<div id="post-61044-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The use of <code>tunnel=building_passage</code> for indoor features is incorrect. The tag is intended for "tunnels though a building" such as <a href="https://wiki.openstreetmap.org/wiki/File:Wullersdorf_Pfarrhof_Durchfahrt.jpg">this example</a> – never features inside a building.</p>
</div>
<div id="comment-61044-info" class="comment-info">
<span class="comment-age">(06 Dec '17, 18:42)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-61029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61029-form-container" class="comment-form-container">
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

