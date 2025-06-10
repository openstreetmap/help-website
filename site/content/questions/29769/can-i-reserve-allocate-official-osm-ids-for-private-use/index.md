+++
type = "question"
title = "Can I reserve / allocate official osm ids for private use?"
description = '''Dear community, we currently are creating indoor maps for our university campus. Unfortunately we are not allowed to upload all this data to the official OSM servers, but we had to set up our own one. Since we can&#x27;t use the official one, we made the database and the processes working with its data t...'''
date = "2014-01-12T17:02:00Z"
lastmod = "2014-01-13T17:14:00Z"
weight = 29769
keywords = [ "josm", "id", "private", "allocate" ]
aliases = [ "/questions/29769" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Can I reserve / allocate official osm ids for private use?](/questions/29769/can-i-reserve-allocate-official-osm-ids-for-private-use)

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
<span id="post-29769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29769-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear community,</p>
<p>we currently are creating indoor maps for our university campus. Unfortunately we are not allowed to upload all this data to the official OSM servers, but we had to set up our own one. Since we can't use the official one, we made the database and the processes working with its data to work with negative osm ids.</p>
<p>The problem now is that JOSM behaves as following: When creating new elements these elements get negative ids. Once the just-saved file gets loaded, all negative ids within it will be replaced with new negative ids. That means there's no consistency of the same file thanks to JOSM.</p>
<p>So my question is: Is there a way to reserve / allocate "real" OSM-IDs for the created ways, relations and nodes without uploading the data itself.</p>
<p>I assume we could just upload a node/way/relation without containing useful information, but I'm frightened someone could remove due to its uselessness and the very same ID could be assigned to some other element.</p>
<p>And since our database data is not stativ but will be upgraded from time to time we cannot just chose any positive ID not yet included in the database because some day it might.</p>
<p>Any help is welcome! Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-private" rel="tag" title="see questions tagged &#39;private&#39;">private</span> <span class="post-tag tag-link-allocate" rel="tag" title="see questions tagged &#39;allocate&#39;">allocate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '14, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/34c0a69c5e95a6e56de49aa65cf845e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henry%20Moews&#39;s gravatar image" />
<p><span>Henry Moews</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henry Moews has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29769" class="comments-container">
<span id="29780"></span>
<div id="comment-29780" class="comment">
<div id="post-29780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not a very good idea to work with negative IDs. Editing software all expect negatives to be NEW items without real IDs assigned yet.</p>
</div>
<div id="comment-29780-info" class="comment-info">
<span class="comment-age">(12 Jan '14, 21:22)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-29769" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29769-form-container" class="comment-form-container">
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

<span id="29772"></span>

<div id="answer-container-29772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29772-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-29772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry, but AFAIK there is no way to reserver/lock IDs without real payload.</p>
<p>If you start from an empty dataset, you might use your own (nonnegative) IDs and keep them in a local xml file. Another way would be to setup your own <a href="http://wiki.openstreetmap.org/wiki/Rails_Port">rails port server</a> with own API etc. that keeps your stuff seperated from OSM DB, while allowing multiple users to edit this data.</p>
<p>I'm not an expert but I guess there might be <a href="http://wiki.openstreetmap.org/wiki/Legal_FAQ">legal problems</a> if you mix OSM data with non free (as you aren't allowed to publish) informations on a dataset level.<br />
</p>
<p>There is also a small but nice existing <a href="http://wiki.openstreetmap.org/wiki/Indoor">indoor community</a> at OSM :)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '14, 18:20</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></p>
</div>
</div>
<div id="comments-container-29772" class="comments-container">
<span id="29776"></span>
<div id="comment-29776" class="comment">
<div id="post-29776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing out the legal problems. Indeed, we're working with these indoor definitions.</p>
</div>
<div id="comment-29776-info" class="comment-info">
<span class="comment-age">(12 Jan '14, 19:52)</span> <span class="comment-user userinfo">Henry Moews</span>
</div>
</div>
</div>
<div id="comment-tools-29772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29772-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29775"></span>

<div id="answer-container-29775" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29775-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use positive IDs for your own data file, starting at 1. If you need to mix your data with data from OSM for some processing, use a small script to re-number your file to using IDs above the highest in OSM at that time.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '14, 19:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29775" class="comments-container">
<span id="29777"></span>
<div id="comment-29777" class="comment">
<div id="post-29777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, actually the data gets immediately in touch with (our own) OSM database. But your idea of re-numbering made me think of re-numbering all of our own OSM elements in the database whenever we update from the official OSM servers having an ID conflict.</p>
</div>
<div id="comment-29777-info" class="comment-info">
<span class="comment-age">(12 Jan '14, 19:57)</span> <span class="comment-user userinfo">Henry Moews</span>
</div>
</div>
<span id="29808"></span>
<div id="comment-29808" class="comment">
<div id="post-29808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>appending to Frederik's hint:</p>
<p>can this be a solution? <a href="http://www.geofabrik.de/en/projects/separatedata/index.html">http://www.geofabrik.de/en/projects/separatedata/index.html</a></p>
</div>
<div id="comment-29808-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 17:14)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-29775" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29775-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29779"></span>

<div id="answer-container-29779" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29779-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Reserving IDs is a <em>very bad</em> idea... Aside from the obvious management complications, there are other complications whenever you encounter conflicts of IDs, software not aware of the reservations, etc.</p>
<p>Also, you're trying to use a tool (JOSM) that wasn't designed to work with "mixed" (OSM and private) data. JOSM will keep renumbering your IDs internally, and it wouldn't matter to it, because even if different between different loads of the same file, it'll be consistent <em>at the moment of the upload</em> to the OSM servers (which will replace the negative numbers with valid IDs)</p>
<p>The ID that'll be used is the next sequence number of the relevant tables. If by some reason the upload fails, the whole transaction is rolled back and the IDs used are "lost" forever.</p>
<p>However, not everything is lost... One workaround I thought is relatively simple, emulates the reservation system, but has some limitations. Let me explain...</p>
<ul>
<li>Change the sequences in your local copy of the OSM database, setting the next value to a <strong>very high</strong> number. The IDs are all bigints, use something like 1 x 10^18, totally out of reach of anything that "normal" OSM will reach in the next billion years. And still leaving trillions of IDs for your usage.</li>
<li>Install the full rails port, including the APIDB server, etc.</li>
<li>Modify JOSM to point to your LOCAL server. Very easy, in the configurations. Maybe, even change the look and feel (also in the configurations) to make clear that data processed with this version should NEVER be uploaded to the public servers.</li>
<li>Add your data and upload to your LOCAL server.</li>
<li>Update using the daily/hourly/minutely from the official OSM.</li>
</ul>
<p>The limitations are:</p>
<ul>
<li>Your data will never be compatible again with the OSM data without more processing - the IDs would have to be stripped and replaced with negative IDs before it could be uploaded to the public OSM server. And probably there'll be many conflicts. Maybe someone else will do a survey and upload some version of a map to the same place?</li>
<li>Your data will have to be <em>fully new</em>. Not even one node, one way can be shared with the public OSM database, not because of copyright, but because if someone changes this item in the public OSM database, your private data will be changed as well, probably in ways that you do not intend to.</li>
<li>If someone else uploads something in the area you privately mapped, it'll overlap your data, and you can't remove it without almost surely breaking the possibility of further updates to you LOCAL database, because it'll fail when it doesn't find the conflicting items.</li>
</ul>
<p>Updates to the APIDB using osmosis, or other tools, from the daily/hourly/minutely changes all come with the IDs already assigned, therefore the sequence number is never touched when you apply them. Your own changes, on the other hand, do not have valid IDs yet, and the API server will use the default (implicit or explicit, can't remember) of the ID column which is "nextval([name_of_sequence])".</p>
<p>EDIT: I didn't fully understood Frederick's answer cited before. Corrected!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '14, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '14, 21:15</strong> </span></p>
</div>
</div>
<div id="comments-container-29779" class="comments-container">
&#10;</div>
<div id="comment-tools-29779" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29779-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29789"></span>

<div id="answer-container-29789" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29789-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Why do you even worry about conflicting IDs if you don't intend to upload your results anyway ? Put your objects in your own db, and use a mashup to display your indoor map on top of the osm basemap.</p>
<p>You can "seed" your work using an extract of OSM data if you want, say the town your school resides in. That would just be a snapshot of osm data; updating said data after you modified it <a href="http://wiki.openstreetmap.org/wiki/Osmosis">should be possible</a>, but is likely to run into problems now and then. Also, remember that if you seed your own map this way, it certainly constitute a derived work and you would <a href="http://wiki.openstreetmap.org/wiki/Legal_FAQ#3b._If_I_have_data_derived_from_OSM_data.2C_do_I_have_to_distribute_it.3F">have to redistribute it</a>, making the whole effort of keeping your work separate a bit pointless.</p>
<p>If you ever want to merge your data with the osm data (assuming you didn't seed it with osm data, and kept it separate), just extract your db as a *.osm file, negate all the ids, load it into josm, check for problems, and upload to osm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '14, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29789" class="comments-container">
<span id="29790"></span>
<div id="comment-29790" class="comment">
<div id="post-29790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can't upload to your own local DB <em>and update it from the diffs</em> unless you take care about conflicting IDs.</p>
</div>
<div id="comment-29790-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 10:08)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="29797"></span>
<div id="comment-29797" class="comment">
<div id="post-29797-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's part of the problems you could have. You'd have to fix them manually on a case by case basis.</p>
<p>Not that I'm advocating this method. I really think you should either upload directly to osm, or use a completely separate db.</p>
</div>
<div id="comment-29797-info" class="comment-info">
<span class="comment-age">(13 Jan '14, 12:45)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-29789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29789-form-container" class="comment-form-container">
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

