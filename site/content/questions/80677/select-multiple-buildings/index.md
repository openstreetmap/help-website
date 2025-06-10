+++
type = "question"
title = "Select multiple buildings"
description = '''I want to do a bulk edit on a huge number of small buildings. How can I select multiple buildings to do that? Clicking them all individually I just tried, spend 10 minutes on it, and then my selection got discarded silently without any warning, and without the possibility to undo that. Fix this plea...'''
date = "2021-06-24T00:31:00Z"
lastmod = "2021-06-24T15:59:00Z"
weight = 80677
keywords = [ "editing" ]
aliases = [ "/questions/80677" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Select multiple buildings](/questions/80677/select-multiple-buildings)

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
<span id="post-80677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80677-score" class="post-score" title="current number of votes">
-12
</div>
<span id="post-80677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to do a bulk edit on a huge number of small buildings. How can I select multiple buildings to do that?</p>
<p>Clicking them all individually I just tried, spend 10 minutes on it, and then my selection got discarded silently without any warning, and without the possibility to undo that. Fix this please!! I'm quite annoyed by this, frankly.</p>
<p>So how to do this properly?</p>
<p>If I drag a selection around them, it only selects "points", the nodes that make up a building. But not the buildings themselves. There's also no filter. I would ideally first unclutter the editing map to hide features I'm not interested in editing. Then drag a selection around the buildings, and have that select <em>buildings</em>, not the nodes that make up buildings.</p>
<p>Also, searching doesn't really work. I was hoping to search by tag or something and do a bulk action from there, but no.</p>
<p>What is the best way to do this?</p>
<p>/edit btw I'm trying the iD editor. I also tried JOSM, but my goggly goodness that is a piece of crap. Sorry, but it really is. It lives in 1993 and it's just... Ugh. Nope, I won't be using that anymore. Multiselecting with the iD editor seems the way to go. Shouldn't be that hard either, really.</p>
<p>Specially what I need to do: select ALL buildings dragging a selection around them, then filter that selection by a specific tag (generic building, not house/apartment/whatever). How hard can it be??</p>
<p>/edit2 Even when hiding ALL features except building, the draggy selection tool insists on selection points, and NEVER any buildings. And I just discovered it also only works (incorrectly) when zoomed in. But seriously, how does it manage to select features that I've hidden? And not select other features (that aren't points) that ARE hidden? Why can't it just bloody select buildings?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '21, 00:31</strong></p>
<img src="https://secure.gravatar.com/avatar/7ef8697a6d7e0d32d9249e002d2e7fda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thanatica&#39;s gravatar image" />
<p><span>Thanatica</span><br />
<span class="score" title="57 reputation points">57</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thanatica has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '21, 01:20</strong> </span></p>
</div>
</div>
<div id="comments-container-80677" class="comments-container">
<span id="80679"></span>
<div id="comment-80679" class="comment">
<div id="post-80679-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For the record, I see that you have created issues in the iD repository, it's probably the best course to solve your problem using only that software.</p>
<p>Please refrain from using harsh words about a project on which a lot of people invest a lot of time ! And IMHO JOSM is the best OSM editor available, maybe I live in 1993... I could use some harsh about iD, but only in private. ;-)</p>
<p>Regards.</p>
</div>
<div id="comment-80679-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 10:31)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="80682"></span>
<div id="comment-80682" class="comment">
<div id="post-80682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FWIW I've voted the question up since in among the JOSM UI hate there are some valid questions being asked.</p>
<p>The right tool for the job here rather depends on what the job is - if it's "select a few things to make the same changes to each" than iD will work just fine; if it's "perform a complicated overpass query to only select certain objects and then change them" then it's either JOSM or use overpass externally and go into iD once per object (which is probably not the best approach).</p>
<p>Also if you're making "the same sort of change" to lots of things then you'll definitely want to explore using the JOSM validator to list other things worth investigating. Not all of them will be errors, but they'll all be worth looking at.</p>
</div>
<div id="comment-80682-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 10:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80687"></span>
<div id="comment-80687" class="comment">
<div id="post-80687-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>As others have said, making derogatory comments about editors is unlikely to encourage people to help you with your issue. Furthermore the people creating these editors are real people &amp; they can really do without this kind of comment: we have certainly had maintainers stop because of this kind of thing.</p>
</div>
<div id="comment-80687-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 12:57)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="80693"></span>
<div id="comment-80693" class="comment not_top_scorer">
<div id="post-80693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Mates, I can't even move the map by dragging, or make a selection in lasso mode. It keeps moving nodes. Yes, nodes are EVERYWHERE, so how can I not select a node?? JOSM is awful, and that is not my opinion. It's measurably crap.</p>
<p>The thing is, since people put so much of their time in these projects, I would expect something better. Surely, they too would want their stuff to work brilliant, wouldn't they? It's no use being all happy and dandy about it if it's broken.</p>
</div>
<div id="comment-80693-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:41)</span> <span class="comment-user userinfo">Thanatica</span>
</div>
</div>
<span id="80696"></span>
<div id="comment-80696" class="comment">
<div id="post-80696-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20408/thanatica"></a><a href="https://help.openstreetmap.org/users/20408/thanatica">@Thanatica</a></p>
<ol>
<li>You move the map by dragging with [RMB].</li>
<li>Explain how you can't lasso select?</li>
<li>There's a Unselect Node button and hotkey.</li>
<li>In search, you add <code>type:way</code> or <code>-type:node</code> to Select or Add; use <code>type:way</code> in Find In Selection; or use <code>type:node</code> in Remove From Selection.</li>
</ol>
<p>Throwing your "crap" at it with such "awful" attitude is not going to solve your "broken" problem.</p>
</div>
<div id="comment-80696-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:47)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="80697"></span>
<div id="comment-80697" class="comment">
<div id="post-80697-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20408/thanatica">@Thanatica</a> Perhaps it's worth taking a step back and asking yourself after posting that "measurably crap" comment? Do you actually want anyone to help you, or not? If not, then there are probably better places on the Internet set to provoke an argument. I hear Twitter is popular these days.</p>
<p>If, on the other hand you actually want someone to help you to do what you want to do in OSM then it's worth listening to people suggest, not merely saying "I want X to do Y. No, I will not use Z (which does Y)".</p>
</div>
<div id="comment-80697-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80677" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-80677-form-container" class="comment-form-container">
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

<span id="80678"></span>

<div id="answer-container-80678" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80678-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-80678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you want to do is advanced editing that cannot be done with ID editor. JOSM is the advanced editing tool for OSM. It's neither beautiful nor intuitive, but it is the right program for your task. If you can bring yourself to use JOSM, I'd be happy to help you accomplish this task with it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ec46821d791b304a5c3c9380ab661d11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Discostu36&#39;s gravatar image" />
<p><span>Discostu36</span><br />
<span class="score" title="236 reputation points">236</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Discostu36 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80678" class="comments-container">
<span id="80681"></span>
<div id="comment-80681" class="comment">
<div id="post-80681-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've not voted this down because you offered to help, but the first part of this answer isn't actually correct since selecting multiple things in iD to make changes to them is actually very straightforward.</p>
</div>
<div id="comment-80681-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 10:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80684"></span>
<div id="comment-80684" class="comment">
<div id="post-80684-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanatica specifically asked for "selection by a specific tag (generic building, not house/apartment/whatever)", this is not possible with ID.</p>
</div>
<div id="comment-80684-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 11:49)</span> <span class="comment-user userinfo">Discostu36</span>
</div>
</div>
<span id="80686"></span>
<div id="comment-80686" class="comment">
<div id="post-80686-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>True, that was one of the other things asked lower down, but the first line of the question is literally "I want to do a bulk edit on a huge number of small buildings. How can I select multiple buildings to do that?".</p>
</div>
<div id="comment-80686-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 12:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="80694"></span>
<div id="comment-80694" class="comment">
<div id="post-80694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried JOSM. It's awful. And it too silently discards a selection if I happen to do something that JOSM thinks in its infinite brilliance should discard any selection, of course without the possibility to ctrl+z it.</p>
<p>iD at least has somewhat of an intuitive GUI, if it could be bothered to not select things I've hidden away, and (again) not silently discard a painstakingly made selection!</p>
</div>
<div id="comment-80694-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:43)</span> <span class="comment-user userinfo">Thanatica</span>
</div>
</div>
</div>
<div id="comment-tools-80678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80680"></span>

<div id="answer-container-80680" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80680-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-80680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I was confused, so I checked - you can make changes to multiple things with iD (and with Potlatch, and with JOSM). In iD use "shift select" to select more that one item. <a href="https://www.openstreetmap.org/changeset/106889113">https://www.openstreetmap.org/changeset/106889113</a> is the test change, by the way.</p>
<p>However, it's absolutely true that there are some things that you can do in JOSM that you can't do in iD, and that's by design - with JOSM it's fairly easy for people unfamiliar with what they're doing to accidentally change things they weren't expecting to (examples including "adding a tag to all nodes in a multi-select as well as all ways" and "accidentally dragging everything in a large area somewhere else").</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-80680" class="comments-container">
<span id="80695"></span>
<div id="comment-80695" class="comment">
<div id="post-80695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Shift select works by having to click on each and every feature individually. And like I said, one misclick and the whole selection is gone. POOF.</p>
</div>
<div id="comment-80695-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:45)</span> <span class="comment-user userinfo">Thanatica</span>
</div>
</div>
</div>
<div id="comment-tools-80680" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80680-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80692"></span>

<div id="answer-container-80692" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80692-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-80692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To elaborate:</p>
<ol>
<li>JOSM Vanilla allows seeing and selecting selection history. (This is not "undo" since it's not an actual "edit")</li>
<li>JOSM Vanilla allows searching by tags and other metadata; by various syntax (viz RegEx and MapCSS additionally); to include, exlude, or find within selected objects.</li>
<li>JOSM Vanilla has a lasso select tool.</li>
<li>JOSM's Utilsplugin2 has a Select All Inside tool for areas. (And, Unselect Nodes)</li>
<li>iD has such loading behavior when zooming far away. This is an inherent limitation. To compare, JOSM further has a Continous Download plugin (and Download Along); on top of downloading data or opening files, including loading from Overpass Turbo query.</li>
<li>JOSM has a powerful filter working the same as the search function, to hide different objects. (Using a <code>-type:node</code> hide filter will allow you to see, select, and edit only lines in the main interface)</li>
</ol>
<p>Conclusion: Yes, JOSM is the solution. No, it's not "goggly goodness that is a piece of crap. Sorry, but it really is. It lives in 1993 and it's just... Ugh.". If you don't want to use it, it's your choice. Don't blame, let alone shit on anyone. "Multiselecting with the iD editor seems the way to go." is ultimately untrue, for all the design and use concerns here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '21, 16:20</strong> </span></p>
</div>
</div>
<div id="comments-container-80692" class="comments-container">
<span id="80698"></span>
<div id="comment-80698" class="comment">
<div id="post-80698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not balming anyone personally. I don't even know who made it. If I conclude a program is crap, I am free to let people know, thank you very much.</p>
<p>So the question remains: how to I easily multiselect a whole bunch of features, without my selection going POOF at some arbitrary point, and having that selection tool actually selecting what I'm seeing on the map, not what is hidden?</p>
<p>The answer is: JOSM can't do that. No, it just bloody can't. I can't make a selection by dragging. You may claim it can, but it's kjust not possible in practice. iD also can't do it. What remains is a LOT of work for me, and frankly I will not be doing that.</p>
<p>I'm willing to if I can just bloody select things properly. Isn't that supposed to be one of the most basic features of map editing?!</p>
</div>
<div id="comment-80698-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:49)</span> <span class="comment-user userinfo">Thanatica</span>
</div>
</div>
<span id="80699"></span>
<div id="comment-80699" class="comment">
<div id="post-80699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/20408/thanatica"></a><a href="https://help.openstreetmap.org/users/20408/thanatica">@Thanatica</a> Ok I see your problem. If you are so concerned, you need to make a <code>type:node</code> hide filter to hide all points. Then you can select only lines directly.</p>
<p>A possible reason for not implementing a direct action yet is it could match at least my workflow better. I'm not going to toggle filters, or press more buttons when selecting every time. If I want to do it simple, I use Unselect Nodes. If I need it complex, I use Search. You can definitely check and comment on any open tickets for adding functions in JOSM.</p>
<p>Do you get how explaining clearly or checking yourself can help solve an issue now? Much more useful than unloading a bunch of "crap" upfront.</p>
</div>
<div id="comment-80699-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:53)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="80700"></span>
<div id="comment-80700" class="comment">
<div id="post-80700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/16887/kovoschiz"></a><a href="https://help.openstreetmap.org/users/16887/kovoschiz">@Kovoschiz</a> Actually, it'd be really useful to either create an OSM diary entry explaining those steps in JOSM in a bit more detail. For example "JOSM Vanilla allows seeing and selecting selection history" doesn't really explain to someone how to do that. A web search for "josm selection history" finds a <a href="https://wiki.openstreetmap.org/wiki/JOSM/Basic_editing">couple</a> <a href="https://wiki.openstreetmap.org/wiki/JOSM/Advanced_editing">of</a> pages, but doesn't find the <a href="https://josm.openstreetmap.de/wiki/Help">JOSM help</a> at all. I've never found searching <a href="https://josm.openstreetmap.de/search?q=selection+history">within</a> the JOSM help especially useful.</p>
<p>In terms of what exists now, <a href="https://learnosm.org/en/josm/start-josm/">Learnosm's pages</a> are a good a place to start as any.</p>
</div>
<div id="comment-80700-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 15:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-80692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80692-form-container" class="comment-form-container">
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

