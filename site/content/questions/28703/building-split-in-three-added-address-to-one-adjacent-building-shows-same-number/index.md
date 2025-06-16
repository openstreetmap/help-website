+++
type = "question"
title = "Building split in three, added address to one, adjacent building shows same number"
description = '''Hi, in trying to add my employer&#x27;s office to OSM, I split the large building that contains the office into three using JOSM&#x27;s utils2 plugin. I added the address including housenumber to the middle building and also added a point tagged with company information. Now OSM shows two buildings with the s...'''
date = "2013-12-02T19:56:00Z"
lastmod = "2013-12-08T00:40:00Z"
weight = 28703
keywords = [ "building", "relation", "split", "housenumbering" ]
aliases = [ "/questions/28703" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Building split in three, added address to one, adjacent building shows same number](/questions/28703/building-split-in-three-added-address-to-one-adjacent-building-shows-same-number)

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
<span id="post-28703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28703-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>in trying to add my employer's office to OSM, I split the large building that contains the office into three using JOSM's utils2 plugin. I added the address including housenumber to the middle building and also added a point tagged with company information. Now OSM shows two buildings with the same housenumber. Even giving that second building its own housenumber does make the correct number show up.</p>
<p>Here's a map link: <a href="https://www.openstreetmap.org/way/56002419#map=19/48.13039/11.61799">https://www.openstreetmap.org/way/56002419#map=19/48.13039/11.61799</a> This is the adjacent building with the wrong number, it should be 62. The 64 to the right is correct and that is the number I originally created.</p>
<p>Thanks for any help,</p>
<p>Sebastian</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-housenumbering" rel="tag" title="see questions tagged &#39;housenumbering&#39;">housenumbering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '13, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/71bd4f4322c93e7fdcf3681da540fed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Unic-com&#39;s gravatar image" />
<p><span>Unic-com</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Unic-com has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Dec '13, 12:48</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span></p>
</div>
</div>
<div id="comments-container-28703" class="comments-container">
<span id="28729"></span>
<div id="comment-28729" class="comment">
<div id="post-28729-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is really odd. I "dirtied" the tile to force re-rendering, and the 64 disappeared, but so did the building! I wonder if something in the rendering chain changed?</p>
</div>
<div id="comment-28729-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:14)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
<span id="28731"></span>
<div id="comment-28731" class="comment">
<div id="post-28731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would guess that these objects did not make to the renderers db for some reason. After a version change of these objects the buildings should reappear (hopefully)</p>
</div>
<div id="comment-28731-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:27)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="28745"></span>
<div id="comment-28745" class="comment">
<div id="post-28745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, the rendering hasn't changed so far (well, I didn't see the intermediate stage that neuhausr mentioned, what I mean is that the rendering is back in the state I saw it). I've seen what was meant by RM87's answer below, but the number 64 still gets rendered for all the three buildings that were previously members of the old relation. I don't understand what RM87 means by version change, can this be triggered somehow?</p>
</div>
<div id="comment-28745-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 22:37)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
<span id="28794"></span>
<div id="comment-28794" class="comment">
<div id="post-28794-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Now something probably similar to the state described by neuhausr can be seen. At the smallest zoom level, the building seems to be cut off, at two levels smaller and above they don't appear at all. Could someone(TM) do something please? Thanks ...</p>
</div>
<div id="comment-28794-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 00:45)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
<span id="28795"></span>
<div id="comment-28795" class="comment">
<div id="post-28795-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think it is all correct too and that the map tiles are still awaiting rendering for whatever reason.<br />
<a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">https://help.openstreetmap.org/questions/178/how-often-does-the-main-mapnik-map-get-updated</a></p>
<p>A search for 62 Berg-am-Laim-Straße, München or 64 Berg-am-Laim-Straße, München will find the correct location.</p>
</div>
<div id="comment-28795-info" class="comment-info">
<span class="comment-age">(05 Dec '13, 02:08)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="28888"></span>
<div id="comment-28888" class="comment not_top_scorer">
<div id="post-28888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks fine now. I see that nevw has made changes – is it correct that you more or less "touched" the existing objects but did not really change anything? Anyway, thanks and as this is my first use of the OSM help system I'm wondering about the "award points" feature. It seems that RM87's answer was right all along and I've just upvoted it. I see that I can also "award points" but don't know if I should and how many points are usually awarded. Also I've clicked the "great comment" icon next to nevw's answer but don't know if this the right kind of response and/or whether to "award points".</p>
</div>
<div id="comment-28888-info" class="comment-info">
<span class="comment-age">(07 Dec '13, 21:07)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
<span id="28900"></span>
<div id="comment-28900" class="comment not_top_scorer">
<div id="post-28900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wrote the previous comment before I noticed that nevw had already sent me a message. He basically tried to trigger rerendering by adding extra nodes. I've now deleted these nodes and it still looks fine on all zoom levels. Great.</p>
</div>
<div id="comment-28900-info" class="comment-info">
<span class="comment-age">(08 Dec '13, 00:22)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
<span id="28902"></span>
<div id="comment-28902" class="comment not_top_scorer">
<div id="post-28902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can't figure out how to close a question, or indeed how to send a user a personal message. I'll stop trying for now.</p>
</div>
<div id="comment-28902-info" class="comment-info">
<span class="comment-age">(08 Dec '13, 00:40)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
</div>
<div id="comment-tools-28703" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-28703-form-container" class="comment-form-container">
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

<span id="28726"></span>

<div id="answer-container-28726" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28726-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28726-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28726-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Unic-com has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There was one unnecessary <a href="https://www.openstreetmap.org/relation/1319742">multipolygon relation</a> that had that building as single outer member. After you split the building in three the relation bonded these three buildings into one in some strange way.</p>
<p>It should appear normal soon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Dec '13, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RM87 has 20 accepted answers">22%</span> </br></p>
</div>
</div>
<div id="comments-container-28726" class="comments-container">
<span id="28901"></span>
<div id="comment-28901" class="comment">
<div id="post-28901-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>As far as I can see, this was the key observation that would have solved everything immediately if OSM had not suddenly decided to act strangely with regard to rerendering. I'll see if I can close this question now. Thanks.</p>
</div>
<div id="comment-28901-info" class="comment-info">
<span class="comment-age">(08 Dec '13, 00:27)</span> <span class="comment-user userinfo">Unic-com</span>
</div>
</div>
</div>
<div id="comment-tools-28726" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28726-form-container" class="comment-form-container">
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

