+++
type = "question"
title = "Matching new roads to the network"
description = '''Very soon i&#x27;m gonna have big amount of data with high accuracy for roads that are not registered in Uganda. The goal is to contribute to OSM by giving them out. My first idea was to collect gpx track and them turning them into roads with potlatch 1 However it doesn&#x27;t seem to connect them to the road...'''
date = "2018-06-02T07:43:00Z"
lastmod = "2018-06-04T10:13:00Z"
weight = 63955
keywords = [ "roads", "matching", "gps" ]
aliases = [ "/questions/63955" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Matching new roads to the network](/questions/63955/matching-new-roads-to-the-network)

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
<span id="post-63955-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63955-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63955-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Very soon i'm gonna have big amount of data with high accuracy for roads that are not registered in Uganda. The goal is to contribute to OSM by giving them out.</p>
<p>My first idea was to collect gpx track and them turning them into roads with potlatch 1 However it doesn't seem to connect them to the road network, as they look "on top" of it.</p>
<p>I come here to find some help from contributors and/or developers : what is the best way to add new roads from GPS data ? We're having high-accuracy AND big amount of data : it is not possible to correct by hand everything.</p>
<p>Thanks in advance, and if I find my solutions we'll have hundreds of km registered in Uganda :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '18, 07:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9ad06e49c4c03e29b6220d4bd8512c07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucien%20Pineau&#39;s gravatar image" />
<p><span>Lucien Pineau</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucien Pineau has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63955" class="comments-container">
<span id="64000"></span>
<div id="comment-64000" class="comment">
<div id="post-64000-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, after a few answers, let me correct my question: - let's say I have a lot of already corrected road, with right tags and stuff. - Those roads match satellites imagery and represents actual roads</p>
<p>My question is then : how to connect all of them automatically to a new/existing node on the crossing roads ?</p>
</div>
<div id="comment-64000-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:20)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
<span id="64002"></span>
<div id="comment-64002" class="comment">
<div id="post-64002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You don't do it "automatically". You do it by hand.</p>
</div>
<div id="comment-64002-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:25)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64003"></span>
<div id="comment-64003" class="comment">
<div id="post-64003-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is crazy no one never created a tool to do this ? It's not a big problem it's just gonna take time but i'm surprised that no one never thought of making this automatic,thanks for the answers by the way</p>
</div>
<div id="comment-64003-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:32)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
<span id="64004"></span>
<div id="comment-64004" class="comment">
<div id="post-64004-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sure there are. There's a reason we have <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct</a></p>
</div>
<div id="comment-64004-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:42)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64005"></span>
<div id="comment-64005" class="comment not_top_scorer">
<div id="post-64005-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll also recommend looking into <a href="https://wiki.openstreetmap.org/wiki/JOSM">https://wiki.openstreetmap.org/wiki/JOSM</a> . For mass editing roads etc, it can be very helpful</p>
</div>
<div id="comment-64005-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:45)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64006"></span>
<div id="comment-64006" class="comment not_top_scorer">
<div id="post-64006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks, do you have alink or something ? In parallel i'm contacting the local OSM communtiy to discuss for an action plan</p>
</div>
<div id="comment-64006-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:47)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
<span id="64009"></span>
<div id="comment-64009" class="comment not_top_scorer">
<div id="post-64009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A link for?</p>
</div>
<div id="comment-64009-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 09:37)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="64012"></span>
<div id="comment-64012" class="comment">
<div id="post-64012-score" class="comment-score">
4
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15202/lucien-pineau">@Lucien Pineau</a> please don't use answers to expand/refine your question.</p>
<p>Back to the original question: connecting up the road network is really something best done manually for QA reasons (and it is something that humans are relatively good and fast at). It is not that it can't be done automatically it is that we have a large body of experience that says your proposal to do so is an accident waiting to happen (which when happened will require people to manually go over all the stuff automatically added and fix it, which is a lot more work than doing it properly the first time).</p>
<p>You don't need to do it alone, for example you could create a task on one of the task managers. Or you could simply make the data available in a suitable form.</p>
</div>
<div id="comment-64012-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 10:13)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63955" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63955-form-container" class="comment-form-container">
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

<span id="63960"></span>

<div id="answer-container-63960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63960-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-63960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, if your single test road (the only upload you've done) is anything to go by then it's unfortunately far from desirable. The test road, Way: <a href="https://www.openstreetmap.org/way/592937758">592937758</a> does not seem to line up with any apparent roads on Bing, Esri or DigitalGlobe imagery. It's not connected to the roads it approaches at either end. It has no tags at all to describe it. It really ought to be removed.</p>
<p>I'd suggest reading a guide <a href="https://wiki.openstreetmap.org/wiki/Beginners%27_guide">https://wiki.openstreetmap.org/wiki/Beginners%27_guide</a> to get you started. Then draw each way separately over your uploaded gpx traces, tagging each way appropriately. This page <a href="https://wiki.openstreetmap.org/wiki/Highway_Tag_Africa">https://wiki.openstreetmap.org/wiki/Highway_Tag_Africa</a> is specific to African highways.</p>
<p>Regards Bernard.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '18, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Jun '18, 12:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-63960" class="comments-container">
<span id="63993"></span>
<div id="comment-63993" class="comment">
<div id="post-63993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This was a test for the converter that should even be uploaded... The problem here is I corrected a gpx trace by hand, trying to connect it to the road network, as it it my first problem, but i don't know how to do it</p>
</div>
<div id="comment-63993-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 07:22)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
</div>
<div id="comment-tools-63960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63960-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63956"></span>

<div id="answer-container-63956" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63956-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-63956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short answer; You don't add new roads from GPS data. You're actually supposed to "correct by hand" (see also <a href="https://help.openstreetmap.org/questions/7461/using-a-gps-track-to-create-a-road-or-path).">https://help.openstreetmap.org/questions/7461/using-a-gps-track-to-create-a-road-or-path).</a> I've corrected tons of roads by hand myself and can tell you that with the right tools it's not as bad as you may think.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Jun '18, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-63956" class="comments-container">
<span id="63957"></span>
<div id="comment-63957" class="comment">
<div id="post-63957-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes this subject was read, but as I said, it will be long unsurveyed roads in the rural area, and we will have real GPS, not phones. The only info i could need if I convert gpx to roads, is how to connect them to the road network.</p>
</div>
<div id="comment-63957-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 11:04)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
<span id="63966"></span>
<div id="comment-63966" class="comment">
<div id="post-63966-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Read Hjart's answer again. You <em>should not</em> convert GPX tracks to roads. GPX tracks can be loaded in the editor but tracing them <em>must</em> be done manually.</p>
</div>
<div id="comment-63966-info" class="comment-info">
<span class="comment-age">(02 Jun '18, 16:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="63994"></span>
<div id="comment-63994" class="comment">
<div id="post-63994-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I said, I know, but we have a very accurate GPS and the possibility to have multiple records. My problem is then to not spend hours connecting them to the road network, as they don't need a correction.</p>
</div>
<div id="comment-63994-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 07:26)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
<span id="63996"></span>
<div id="comment-63996" class="comment">
<div id="post-63996-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You will not end up with a navigable road network unless you "spend hours connecting them to the road network". There's no avoiding it.</p>
</div>
<div id="comment-63996-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 07:31)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="63997"></span>
<div id="comment-63997" class="comment">
<div id="post-63997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Get involved with the local community. You don't have to import all of these roads alone. Also make sure to read the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a>.</p>
</div>
<div id="comment-63997-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 07:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="64001"></span>
<div id="comment-64001" class="comment not_top_scorer">
<div id="post-64001-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not doing it alone, the collection of data will be done by a lot of people and that's why i'm searching for the good way of connecting. But if as you said there is no way of connecting them to the road network unless with hands, then... I might get to work now :p</p>
</div>
<div id="comment-64001-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 08:21)</span> <span class="comment-user userinfo">Lucien Pineau</span>
</div>
</div>
</div>
<div id="comment-tools-63956" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63956-form-container" class="comment-form-container">
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

