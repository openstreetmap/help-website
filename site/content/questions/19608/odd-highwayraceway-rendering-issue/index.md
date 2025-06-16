+++
type = "question"
title = "Odd &quot;highway=raceway&quot; rendering issue"
description = '''There seems to be a strange rendering issue that affects only &quot;highway=raceway&quot; ways here: https://www.openstreetmap.org/?lat=53.30779&amp;amp;lon=-0.06335&amp;amp;zoom=16&amp;amp;layers=M  It&#x27;s not appearing in either OSM&#x27;s standard mapnik tiles (or e.g. the cyclemap). It used to until recent edits to the area,...'''
date = "2013-02-06T12:29:00Z"
lastmod = "2015-07-29T18:20:00Z"
weight = 19608
keywords = [ "rendering", "mapnik" ]
aliases = [ "/questions/19608" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Odd "highway=raceway" rendering issue](/questions/19608/odd-highwayraceway-rendering-issue)

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
<span id="post-19608-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19608-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19608-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There seems to be a strange rendering issue that affects only "highway=raceway" ways here:</p>
<p><a href="https://www.openstreetmap.org/?lat=53.30779&amp;lon=-0.06335&amp;zoom=16&amp;layers=M">https://www.openstreetmap.org/?lat=53.30779&amp;lon=-0.06335&amp;zoom=16&amp;layers=M</a></p>
<p><img src="/upfiles/q_2.png" alt="Cadwell Park showing only 1 highway=raceway" /></p>
<p>It's not appearing in either OSM's standard mapnik tiles (or e.g. the cyclemap). It used to until recent edits to the area, but those edits only changed the source tag.</p>
<p>Dirtying tiles has no effect. I did nudge one node on one way ("Coppice") a smidgeon and that way now renders. That would suggest a rendering database issue (but is it strange that the Cyclemap tiles are affected too?).</p>
<p>There are a couple of open trac issues open against highway=raceway (both linked to from <a href="https://trac.openstreetmap.org/ticket/3009">here</a>) but I don't think that either of them is the issue in this case.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '13, 12:29</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '13, 12:30</strong> </span></p>
</div>
</div>
<div id="comments-container-19608" class="comments-container">
<span id="19611"></span>
<div id="comment-19611" class="comment">
<div id="post-19611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>is it because it's split into different ways, and not one loop?</p>
</div>
<div id="comment-19611-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 15:16)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="19621"></span>
<div id="comment-19621" class="comment">
<div id="post-19621-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@neuhausr</span> No, <a href="https://www.openstreetmap.org/?lat=50.55917&amp;lon=11.8152&amp;zoom=17&amp;layers=M">elsewhere</a> it renders fine as single ways and this wouldn't make sense because a raceway doesn't necessarily has to be a loop. <span></span><span>@SomeoneElse</span> An import problem is also the only thing that comes to my mind. I suggest someone having access to the DB taking a look at it. Maybe the cause of the problem can be identified and fixed.</p>
</div>
<div id="comment-19621-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 17:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19622"></span>
<div id="comment-19622" class="comment">
<div id="post-19622-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. One other point (mentioned by EdLoach on IRC) is that "highway=raceway not appearing on the Cycle Map" is a complete red herring. It doesn't appear because it's not supposed to (see <a href="https://www.openstreetmap.org/?lat=52.97871&amp;lon=-1.74134&amp;zoom=16&amp;layers=C">here</a> for example).</p>
</div>
<div id="comment-19622-info" class="comment-info">
<span class="comment-age">(06 Feb '13, 17:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19608" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19608-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="44502"></span>

<div id="answer-container-44502" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44502-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://help.openstreetmap.org/users/5580/th_pro_media">@TH_Pro_Media</a> has identified the nub of the problem, but misidentified the cause.</p>
<p>A quick search <a href="http://overpass-turbo.eu/s/aEe">using Overpass</a> reveals many racetracks tagged with <code>highway=raceway</code> and <code>sport=motor</code> throughout Europe. Indeed, this is an entirely reasonably, albeit redundant, tagging.</p>
<p>Clearly the problem might lie with the CartoCSS rendering. As raceway and motor appear a handful of times in the project it is quite easy to work out if the problem arises with one of these rules: my immediate suspect was <a href="https://github.com/gravitystorm/openstreetmap-carto/search?utf8=%E2%9C%93&amp;q=sport&amp;type=Code">this one</a> in the style file, which says things tagged with sport should be treated as polygons. A quick search revealed a race circuit in Northern Island where parts of the circuit were rendering correctly, but the main racetrack, mapped as a closed way was not. A simple test then was to add an <code>area=no</code> tag which should force the way to be treated as a line. The way now <a href="https://www.openstreetmap.org/#map=15/54.3070/-5.5828">renders correctly</a>. Note, that very few of the ways tagged with <code>sport=motor</code> were closed (8/144).</p>
<p>This rule could conceivable affect other sports which apply to linear ways when such ways are closed (the only one I can think of immediately is climbing on cliffs, but these will likely be tagged <code>area=no</code> when closed).</p>
<p><strong>Summary</strong>: this is a feature of the CartoCSS style which causes raceways mapped as closed ways to be treated as areas when any sport tag is applied. The solutions are either: a) remove the <code>sport=motor</code> tag; or b) add <code>area=no</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '15, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-44502" class="comments-container">
<span id="44503"></span>
<div id="comment-44503" class="comment">
<div id="post-44503-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is this really the preferred solution? Another option could be for the stylesheet to assume <code>area=no</code> even for objects tagged with <code>sport</code> whenever a <code>highway</code> tag is present. I'm not sure which solution should be preferred.</p>
</div>
<div id="comment-44503-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 12:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44517"></span>
<div id="comment-44517" class="comment">
<div id="post-44517-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>FYI, this issue is <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/854">already known</a> over at the OSM-Carto Github. While that issue is titled with sport=running, it covers the use of any sport=* on closed linear ways.</p>
</div>
<div id="comment-44517-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 17:34)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="44520"></span>
<div id="comment-44520" class="comment">
<div id="post-44520-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> thanks: and of course this is the long-term answer for scai, fix the bug in OSM-Carto. area=no is better because it is redundant &amp; does not remove information, whereas dropping sport=motor does</p>
</div>
<div id="comment-44520-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 18:20)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44502-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44500"></span>

<div id="answer-container-44500" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44500-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44500-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44500-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I also came across similar bug where part of raceway is not rendered: <a href="https://www.openstreetmap.org/#map=18/55.51883/25.07223">https://www.openstreetmap.org/#map=18/55.51883/25.07223</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jul '15, 09:06</strong></p>
<img src="https://secure.gravatar.com/avatar/a6980c38dd90e41f83a3ace40f11ffb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pauliusz&#39;s gravatar image" />
<p><span>pauliusz</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pauliusz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44500" class="comments-container">
<span id="44501"></span>
<div id="comment-44501" class="comment">
<div id="post-44501-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Interesting, because there are no relations involved there - just a closed way and a non-closed way.</p>
</div>
<div id="comment-44501-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 09:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-44500" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44500-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19698"></span>

<div id="answer-container-19698" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19698-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19698-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19698-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I fixed it for you. The problem was that you had also tagged the ways with sport=motor. That tag should be used on nodes or closed ways that are also tagged as leisure=track to indicate a use for a sports complex. The tag highway=raceway implies sport=motor so that tag is redundant and incorrect if placed on a highway=raceway way as well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '13, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/2b0c978e72fa940b594e41b8343a023e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TH_Pro_Media&#39;s gravatar image" />
<p><span>TH_Pro_Media</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TH_Pro_Media has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19698" class="comments-container">
<span id="19702"></span>
<div id="comment-19702" class="comment">
<div id="post-19702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, but I'm not convinced that "sport=motor" is the issue. If you have a look at <a href="https://www.openstreetmap.org/?lat=52.82958&amp;lon=-1.37434&amp;zoom=15&amp;layers=M">Donington Park</a>, you'll see that that is tagged like that and doesn't have the same issue.</p>
</div>
<div id="comment-19702-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 17:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19703"></span>
<div id="comment-19703" class="comment">
<div id="post-19703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you take a look at Donington Park??? The highway=raceway ways are not tagged as sport=motor. They are tagged as highway=raceway only that is why they are rendering properly.</p>
</div>
<div id="comment-19703-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 17:46)</span> <span class="comment-user userinfo">TH_Pro_Media</span>
</div>
</div>
<span id="19704"></span>
<div id="comment-19704" class="comment">
<div id="post-19704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://www.openstreetmap.org/browse/way/27131003">Yes</a></p>
</div>
<div id="comment-19704-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 17:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19705"></span>
<div id="comment-19705" class="comment">
<div id="post-19705-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>When I pull up that area in JOSM, there are some ways that are tagged with motor=sport, but most are not. As far as why all of it is rendering properly, my guess is that the "circuit" relation that has been established takes the highway=raceway tag and renders all of the ways in the relation with that.</p>
<p>Regardless, please look at wiki.openstreetmap.org/wiki/sport. That page clearly shows that the sport=motor tag is only useable on nodes and closed ways. Whether it renders properly or not, sport=motor should not be tagged on a linear way.</p>
</div>
<div id="comment-19705-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 18:05)</span> <span class="comment-user userinfo">TH_Pro_Media</span>
</div>
</div>
<span id="19706"></span>
<div id="comment-19706" class="comment">
<div id="post-19706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am going to remove the incorrect tags from Donington Park</p>
</div>
<div id="comment-19706-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 18:06)</span> <span class="comment-user userinfo">TH_Pro_Media</span>
</div>
</div>
<span id="19708"></span>
<div id="comment-19708" class="comment not_top_scorer">
<div id="post-19708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think sport=motor only belongs on <em>closed</em> ways (or nodes). A leisure track doesn't necessarily has to be closed, too.</p>
</div>
<div id="comment-19708-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 20:32)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19710"></span>
<div id="comment-19710" class="comment not_top_scorer">
<div id="post-19710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not arguing about whether the tagging is "correct" or not (I'm quite prepared to believe that the previous tagging wasn't), merely trying to understand why a way wasn't rendering previously but (after a "node move" edit to a way) started to do so.<br />
</p>
<p>Re Donington, <a href="https://www.openstreetmap.org/browse/relation/51164">the relation</a> that the way that had both sport=motor and highway=raceway was part of didn't have highway=raceway on it, so that doesn't explain way the way that I linked to was rendering. I'll have to have a look at the mapnik stylesheet...</p>
</div>
<div id="comment-19710-info" class="comment-info">
<span class="comment-age">(07 Feb '13, 20:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19698" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-19698-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19737"></span>

<div id="answer-container-19737" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19737-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-19737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When something is not rendering properly the first thing that must be discerned is if it is tagged in accordance with the documentation. If you don't know how things are supposed to work, how can you expect to troubleshoot and find the problem?</p>
<p>The reason why I responded to your question is because I spent a bunch of time myself wondering about why my track was not showing up when I tagged the Hilo Dragstrip. I was using the same motor=sport tag on the raceway. Would.not.render until I took that tag off. I found out later that is because it is the wrong type of tag for those kind of ways.</p>
<p>Yes, the wiki specifically states that sport=motor is only for use on nodes and linear ways. That is what the little icons of a node and a closed way next to the sport=motor entry on that page signify.</p>
<p>I believe you are misunderstanding the difference between a linear way and a closed way. In OSM a linear way is a fundamentally different thing than a closed way. A closed way describes an area. A racetrack is not an area. Geometrically it is a "loop" but is is not a "closed polygon." It is constructed of one or more linear ways. They are all connected by node, but it is not a closed poly.</p>
<p>The reason why your ways did not render when you tagged them with motor=sport is that OSM thinks that you are tagging closed areas and sees your "loop of ways" as a bunch of connected, but incomplete/unclosed polys and it cannot render that! That's why the ways did not render before. It thinks it is supposed to be rendering a closed area but you want it to render linear ways in a loop. Did I explain that well enough?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '13, 03:34</strong></p>
<img src="https://secure.gravatar.com/avatar/2b0c978e72fa940b594e41b8343a023e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TH_Pro_Media&#39;s gravatar image" />
<p><span>TH_Pro_Media</span><br />
<span class="score" title="38 reputation points">38</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TH_Pro_Media has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-19737" class="comments-container">
<span id="19743"></span>
<div id="comment-19743" class="comment">
<div id="post-19743-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nah.</p>
<ol>
<li>We <a href="https://wiki.openstreetmap.org/wiki/Tagging_for_the_renderer">don't tag for the renderer</a>.</li>
<li>The documentation is just a wiki. It has errors and is constantly changing.</li>
<li>A simple way and a <em>closed</em> way are not fundamentally different things in OSM. A closed way just has the same start and end nodes, that's all.</li>
<li>A <em>closed</em> way doesn't necessarily describe an <em>area</em>. Alone the tags decide whether a closed way is an area or just an outline. A <a href="https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout">roundabout</a> for example can be mapped both as multiple single ways and as a closed loop, but is usually never an area. In contrast a <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpedestrian">pedestrian</a> way can also be mapped as a single way or a closed loop. But it can be both an area by adding <a href="https://wiki.openstreetmap.org/wiki/Key:area">area=yes</a> or otherwise just an outline.</li>
</ol>
<p>For more information see the rather basic wiki page about <a href="https://wiki.openstreetmap.org/wiki/Elements">OSM's elements</a>.</p>
</div>
<div id="comment-19743-info" class="comment-info">
<span class="comment-age">(08 Feb '13, 07:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="44505"></span>
<div id="comment-44505" class="comment">
<div id="post-44505-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Willowbank speedway is tagged highway=road, <a href="https://www.openstreetmap.org/#map=18/-27.69568/152.65788">https://www.openstreetmap.org/#map=18/-27.69568/152.65788</a> although it has no other use then driving down as fast as. So theyre might be several others around the world on OSM. This one should if possible get highway=raceway, raceway=speedway a different kind of speed sport. It’s not a closed track, by service roads yes, but not as raceway. The direction of the raceway is strange, IMHO drag racing happens with 2 participants on either side of the track, but this has been tagged in the opposite direction.</p>
</div>
<div id="comment-44505-info" class="comment-info">
<span class="comment-age">(29 Jul '15, 14:40)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-19737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19737-form-container" class="comment-form-container">
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

