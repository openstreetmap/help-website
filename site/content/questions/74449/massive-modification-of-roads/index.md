+++
type = "question"
title = "Massive modification of roads"
description = '''We&#x27;re working on a project using OSM files, which is focused on our region: the Basque Autonomous Community. Some months ago, we&#x27;re asked (by the Transportation division of the basque government) to introduce HGV restrictions on some roads. These ones were numerous, but we&#x27;re able to do it manually....'''
date = "2020-04-28T15:29:00Z"
lastmod = "2020-04-30T13:36:00Z"
weight = 74449
keywords = [ "modification", "bulk", "bulk_editing" ]
aliases = [ "/questions/74449" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Massive modification of roads](/questions/74449/massive-modification-of-roads)

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
<span id="post-74449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74449-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We're working on a project using OSM files, which is focused on our region: the Basque Autonomous Community. Some months ago, we're asked (by the Transportation division of the basque government) to introduce HGV restrictions on some roads. These ones were numerous, but we're able to do it manually.</p>
<p>This time we must introduce lots of updates to many roads (we don't know the exact number). These're vehicles' max length, height, weight and width restrictions to primary roads, so there's a way to automate it.</p>
<p>So far, we've been studying alternatives to accomplish the task.</p>
<p>Take region's PBF file and try to parse and modify it using a library. I've tried using Atlas with a Java application, but when loading the map I was thrown the expected OutOfMemoryError exception.</p>
<p>Modify online OSM data programmatically.</p>
<p>What's the best way to do it? Take into account the task can't be done manually...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-modification" rel="tag" title="see questions tagged &#39;modification&#39;">modification</span> <span class="post-tag tag-link-bulk" rel="tag" title="see questions tagged &#39;bulk&#39;">bulk</span> <span class="post-tag tag-link-bulk_editing" rel="tag" title="see questions tagged &#39;bulk_editing&#39;">bulk_editing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '20, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/e8c9fe4a68a700ba0267498ecf9d9b41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanchezingartek&#39;s gravatar image" />
<p><span>sanchezingartek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanchezingartek has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74449" class="comments-container">
&#10;</div>
<div id="comment-tools-74449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74449-form-container" class="comment-form-container">
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

<span id="74454"></span>

<div id="answer-container-74454" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74454-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74454-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-74454-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, do you want to modify the online database for everyone or just your local copy ? I'll focus on the first option.</p>
<p>You'll need to follow the <a href="https://wiki.openstreetmap.org/wiki/Import">Import</a> process, especially discussion with the local community, dedicated account for easy revert and so on.</p>
<p>You'll have to publish the input data for public review, test your process on small area first, ask for comments...</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Level0">Level0</a> is a low-level editor, which might suit your need. JOSM has a lot of power also.</p>
<p>My main concern is how will you identify the correct road to edit ? Roads in OSM are split in numerous parts (on bridges, lane changes and such). And of course what do you do if the data is already present, but different ?</p>
<p>Are you sure a semi-automated process is not possible, like through <a href="https://wiki.openstreetmap.org/wiki/MapRoulette">MapRoulette</a>, or <a href="https://wiki.openstreetmap.org/wiki/Osmose">Osmose</a> ?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Automated_edits">Mechanical edits</a> are really not encouraged, because the risks to mess the data are high.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-74454" class="comments-container">
&#10;</div>
<div id="comment-tools-74454" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74454-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74455"></span>

<div id="answer-container-74455" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74455-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-74455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Agree with everything H_mlet says, but you should really look at the work of Richard on TfL Cycleway data, see <a href="https://lists.openstreetmap.org/pipermail/talk-gb/2020-April/024470.html">talk-gb</a>. This is a rather analogous problem and therefore I would suggest his approach would work for you. It does depend on having good skills in PostgreSQL, PostGIS and PL/pgSQL.</p>
<p>In real practice I would recommend engaging him to consult on the process if that is financially viable.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '20, 17:57</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-74455" class="comments-container">
&#10;</div>
<div id="comment-tools-74455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74455-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74477"></span>

<div id="answer-container-74477" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74477-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your replies.</p>
<p>I'd like to share all the modifications, since they're made by the basque government. For the time being, I'll make changes to a local copy. Once all the changes have been made, I'll publish them, following your recommendations.</p>
<p>I'm going to explain the process I'm following.</p>
<ol>
<li>I download Spain's latest map from geofabrik (<a href="https://download.geofabrik.de/europe/spain-latest.osm.pbf).">https://download.geofabrik.de/europe/spain-latest.osm.pbf).</a></li>
<li>I use osmconvert to crop the map and leave the Basque Autonomous Country: <code>$ osmconvert spain-latest.osm.pbf -b=-3.9853,42.3585,-1.1948,43.5685 -o=euskadi-latest.o5m</code></li>
<li>Filter the map to only highways: <code>$ osmfilter euskadi-latest.o5m --keep="highway=" -o=euskadi-roads-latest.o5m</code></li>
</ol>
<p>Now, my goal is to filter the map and leave only the roads. I've been told to modify from primary to below highways. According to the <a href="https://wiki.openstreetmap.org/wiki/Key:highway">wiki</a>, I guess I'd modify these: primary, secondary, tertiary and road. I'd not modify link roads, special road types, paths, sidewalks, cycleways and lifecycles.</p>
<p>The tags I've been told to modify, with their respective default generic values, are: maxlength (40m), maxheight (4.7m), maxwidth (5m) and maxweight (110t). These values can be extracted from the following gubernamental <a href="https://www.cetm.es/add/BancoDeDocumentos/transportes-especiales/nacional/redes-vehiculos-2019-verte-grupo-1-rgc.pdf">document</a>.</p>
<p>So, I must modify each tag per each highway:</p>
<p><code>$ osmfilter euskadi-roads-latest.o5m --modify-tags="!maxlength and ( highway=primary or =secondary or =tertiary or =road ) add maxlength=40" -o=euskadi-roads-latest-with-maxlength.o5m</code></p>
<p>This statement must be repeated for maxheight, maxwidth and maxweight. The problem here is that I must detect the roads in which there isn't any tag prestablished to avoid override it.</p>
<p>It seems <code>!maxlength</code> won't work... <code>-bash: !maxlength: event not found</code></p>
<p>Other alternatives would be <code>maxlength!=""</code> or <code>maxlength!=null</code>...</p>
<p>Thank you</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Apr '20, 14:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e8c9fe4a68a700ba0267498ecf9d9b41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanchezingartek&#39;s gravatar image" />
<p><span>sanchezingartek</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanchezingartek has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Apr '20, 14:16</strong> </span></p>
</div>
</div>
<div id="comments-container-74477" class="comments-container">
<span id="74510"></span>
<div id="comment-74510" class="comment">
<div id="post-74510-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>First, I must say I've never done any import. But from what I read, here are some humble remarks.</p>
<ul>
<li><p>Your proposed process will generate a lot of conflicts, as you'll be working on outdated data. You should download only a small part, apply your modifications, upload as soon as possible, and then another small part and so on. With visual verification.</p></li>
<li><p>Please read and follow the Import guideline, which means that your process must be documented and discussed on the wiki and the import mailing-list, where experienced people will see it.</p></li>
<li><p>Explicit tagging of implicit road characteristics is usually frowned upon. But there is a tag to say that it's the default speed : <a href="https://wiki.openstreetmap.org/wiki/Key:source:maxspeed">source:maxspeed</a></p></li>
<li><p>Maybe you should add information to this <a href="https://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Maxspeed">page</a>.</p></li>
<li><p>I've had a look a the reference document, I don't see how you can do the conflation. Even assuming that all the refs are in the database, to compute the PK, with the way split everywhere and such, will be a challenge. That's the part of your process that you should test and document the most.</p></li>
</ul>
<p>Best regards, and good luck.</p>
</div>
<div id="comment-74510-info" class="comment-info">
<span class="comment-age">(30 Apr '20, 13:36)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-74477" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74477-form-container" class="comment-form-container">
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

