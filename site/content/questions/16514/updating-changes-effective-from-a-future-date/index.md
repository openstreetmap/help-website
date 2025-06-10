+++
type = "question"
title = "Updating changes effective from a future date"
description = '''I maintain a set of data covering local bus routes. On the 18 November there is a complete network change. What I&#x27;d like to do is start making the changes now but for them only to be visible from 18th November - and likewise the existing data to turn off (so for example if a way which is an existing...'''
date = "2012-09-28T14:47:00Z"
lastmod = "2012-09-29T09:14:00Z"
weight = 16514
keywords = [ "delay", "timed", "editing", "updates" ]
aliases = [ "/questions/16514" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Updating changes effective from a future date](/questions/16514/updating-changes-effective-from-a-future-date)

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
<span id="post-16514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16514-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I maintain a set of data covering local bus routes. On the 18 November there is a complete network change. What I'd like to do is start making the changes now but for them only to be visible from 18th November - and likewise the existing data to turn off (so for example if a way which is an existing bus route changes that bus route number, I want the number to seamlessly change). I know I will have to edit each way - if only to get rid of the old route data - but is it possible to do this? Otherwise I'm going to be REALLY busy on the 18th!!!!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-timed" rel="tag" title="see questions tagged &#39;timed&#39;">timed</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Sep '12, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/5e4e9b65599d9f6d5daefa69110fdfbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StevePO16&#39;s gravatar image" />
<p><span>StevePO16</span><br />
<span class="score" title="86 reputation points">86</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StevePO16 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '15, 14:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-16514" class="comments-container">
&#10;</div>
<div id="comment-tools-16514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16514-form-container" class="comment-form-container">
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

<span id="16515"></span>

<div id="answer-container-16515" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16515-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16515-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16515-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no straightforward way for such a situation. Of course you can start right now and already create the new <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Bus_routes_.28also_trolley_bus.29">bus route relations</a> and add all related streets and the necessary tags. But how to mark these relations as not yet valid?</p>
<ul>
<li>According to the <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Tags">relation</a> wiki page you can add the <em>state=proposed</em> tag. Does any tool handle this correctly? If not it's the tool's fault, but still annoying.</li>
<li>You could leave out important tags, for example the <em>route</em> tag so that the route won't get displayed anywhere. But then quality assurance tools will complain about the relation being invalid and other users may add the missing tags. Better add a <em>note</em> tag explaining the situation.</li>
<li>You could add a <a href="http://wiki.openstreetmap.org/wiki/Key:start_date">start_date=*</a> but I also doubt any tool will handle this correctly.</li>
<li>You could create/update the relations now and upload them later, but this will most likely lead to painful conflicts as the underlaying data can change anytime.</li>
</ul>
<p>I suggest using the <em>state</em> tag as it fits best and create bug reports for any tool which doesn't handle it correctly.</p>
<p>Also note that even if you update the routes on November 18th most tools will take some days or even weeks until the changes will appear. So you could also just wait and update the relations when you have time for it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '12, 16:01</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Sep '12, 16:02</strong> </span></p>
</div>
</div>
<div id="comments-container-16515" class="comments-container">
<span id="16524"></span>
<div id="comment-16524" class="comment">
<div id="post-16524-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>You could leave out important tags, for example the route tag so that the route won't get displayed anywhere. ... Better add a note tag explaining the situation.</p>
</blockquote>
<p>I wouldn't leave out any tags, but incorporate the note into one of the tags of the relations. E.g. type=route + route=busline_after_nov_18_2012 Doing it this way, the route won't get displayed now AND it is very hard for other mappers to overlook the note. (I've seen many times that a mapper fixed a problem and left the note or FIXME tag about the problem on the object.)</p>
</div>
<div id="comment-16524-info" class="comment-info">
<span class="comment-age">(29 Sep '12, 00:10)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="16526"></span>
<div id="comment-16526" class="comment">
<div id="post-16526-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a nice idea, cartinus. Still you should nevertheless use the <em>note</em> and <em>fixme</em> tags as these are the tags most quality assurance tools will look for.</p>
</div>
<div id="comment-16526-info" class="comment-info">
<span class="comment-age">(29 Sep '12, 09:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16515" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16515-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16516"></span>

<div id="answer-container-16516" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16516-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One can use JOSM to create/update the relations and save the edits to your local computer as an OSM change xml file. And then attempt to upload it later and sort out any conflicts...</p>
<p><a href="https://help.openstreetmap.org/questions/4357/resolving-conflicts">https://help.openstreetmap.org/questions/4357/resolving-conflicts</a></p>
<p><a href="http://wiki.openstreetmap.org/wiki/JOSM/Advanced_editing">http://wiki.openstreetmap.org/wiki/JOSM/Advanced_editing</a> has notes about resolving conflicts.</p>
<p>I can't say I've had any experience with it so I don't know how easy/worthwhile to do changes in advance.</p>
<p>So there is a risk that any 'upfront' editing will be for nothing :(</p>
<p>Conflicts only arise on the version numbers of the objects changed, so for example if I add some POIs in the area that won't effect your work, but if someone changes the actual objects you've edited - such as roads (which doesn't happen too much in Portsmouth area these days) then a conflict will arise.</p>
<p>You can't use Potlatch2 to do this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Sep '12, 16:50</strong></p>
<img src="https://secure.gravatar.com/avatar/074785ea4eae108f0e4e89456bf74737?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robbieonsea&#39;s gravatar image" />
<p><span>robbieonsea</span><br />
<span class="score" title="904 reputation points">904</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robbieonsea has 4 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-16516" class="comments-container">
&#10;</div>
<div id="comment-tools-16516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16516-form-container" class="comment-form-container">
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

