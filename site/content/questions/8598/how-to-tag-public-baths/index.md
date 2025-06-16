+++
type = "question"
title = "How to tag public baths?"
description = '''Hello, There are some places in the world where it is a common for people to go into public bath houses. For example there are some villages where people don&#x27;t have water sanitation installed and they go to public baths. Other example - there are places famous with their mineral springs. There are s...'''
date = "2011-10-23T11:58:00Z"
lastmod = "2011-11-05T08:14:00Z"
weight = 8598
keywords = [ "water", "public", "tagging", "bath" ]
aliases = [ "/questions/8598" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag public baths?](/questions/8598/how-to-tag-public-baths)

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
<span id="post-8598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8598-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,<br />
There are some places in the world where it is a common for people to go into public bath houses. For example there are some villages where people don't have water sanitation installed and they go to public baths.<br />
Other example - there are places famous with their mineral springs. There are some public mineral baths as well. They are used mostly for recreational purposes rather than hygienic needs.<br />
Currently I'm using something like that:<br />
</p>
<p>amenity=bath<br />
mineral_water=yes|no<br />
male=yes|no (usually there are gender access restrictions)<br />
female=yes|no<br />
name=(string)<br />
</p>
<p>There are other amenities I don't know how to cover. For example some of the mineral baths are also healthcare centers (sanatoriums). There are different types of mineral water (with different mineral composition). Some places are also SPA centers. Some have pools, other have only showers. Some places offer cold pool other have hot pool. At some pools swimming is forbidden.</p>
<p>There is a lot of useful info that can fit into OSM. Is there some place alredy tagged like that? Do you have any tagging suggestions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-bath" rel="tag" title="see questions tagged &#39;bath&#39;">bath</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '11, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/ca446edd75e87c48db5dd850d9f394a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivanatora&#39;s gravatar image" />
<p><span>ivanatora</span><br />
<span class="score" title="2740 reputation points"><span>2.7k</span></span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="55 badges"><span class="silver">●</span><span class="badgecount">55</span></span><span title="68 badges"><span class="bronze">●</span><span class="badgecount">68</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivanatora has one accepted answer">7%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8598" class="comments-container">
&#10;</div>
<div id="comment-tools-8598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8598-form-container" class="comment-form-container">
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

<span id="8648"></span>

<div id="answer-container-8648" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8648-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ivanatora has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In taginfo, I found:</p>
<ul>
<li>20 POIs with <a href="http://taginfo.openstreetmap.org/tags/?key=amenity&amp;value=public_bath#wiki">amenity=public_bath</a></li>
<li>16 POIs with <a href="http://taginfo.openstreetmap.org/tags/?key=amenity&amp;value=bathhouse#wiki">amenity=bathhouse</a></li>
<li>4 POIs with <a href="http://taginfo.openstreetmap.org/tags/?key=amenity&amp;value=bath#wiki">amenity=bath</a></li>
</ul>
<p><a href="http://en.wikipedia.org/wiki/Public_bathing">Wikipedia</a> uses "public bathing" for the article on this topic. To me, amenity=public_bath would seem best. "Bathhouse" potentially has some negative connotations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Oct '11, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8648" class="comments-container">
&#10;</div>
<div id="comment-tools-8648" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8648-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8603"></span>

<div id="answer-container-8603" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8603-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not only in poor countries, also in Europe, there are public bathhouses where you can get scrubbed, get a massage or similar things. In Austria for example, it was not uncommon not to have a shower or bathroom in the apartment only 40 years ago, and there are several comedy episodes about people finally building one :D Therefore, some of these baths have survived until now, although a little retrofitted.</p>
<p>some helpful tags: If you can swim, you can use leisure=swimmimg_pool <a href="https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dswimming_pool">https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dswimming_pool</a> If it is a plain shower only (like on highway rest areas et al.): amenity=shower <a href="https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dshower">https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dshower</a> there is also a proposed feature: leisure=hot_spring <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/Hot_Spring">https://wiki.openstreetmap.org/wiki/Proposed_features/Hot_Spring</a> - if it is a thermal bath it can be useful and I already used it myself.</p>
<p>Having bathhouses somehow (= not a swimming pool but more than a shower) would be useful. If anyone wants to make a proposal, I will happily support it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '11, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8603" class="comments-container">
<span id="8607"></span>
<div id="comment-8607" class="comment">
<div id="post-8607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Aha! So it was not so uncommon as I though :) What other amenities are there? I've just read the wikipedia articles of the roman thermas and it seems their baths were pretty large complexes with art galleries, shops, restaurants, sport playgrounds, gyms, etc... I doubt there is something like that in present days, but lets count the options.</p>
</div>
<div id="comment-8607-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 07:49)</span> <span class="comment-user userinfo">ivanatora</span>
</div>
</div>
<span id="8608"></span>
<div id="comment-8608" class="comment">
<div id="post-8608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Check out these sites for background info: <a href="http://www.tbilisi.gov.ge/index.php?sec_id=1074&amp;lang_id=ENG">http://www.tbilisi.gov.ge/index.php?sec_id=1074&amp;lang_id=ENG</a> <a href="http://en.wikipedia.org/wiki/Oskar_Lassar">http://en.wikipedia.org/wiki/Oskar_Lassar</a></p>
</div>
<div id="comment-8608-info" class="comment-info">
<span class="comment-age">(24 Oct '11, 08:18)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-8603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8603-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8792"></span>

<div id="answer-container-8792" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8792-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Could your write a proposal for amenity=public_bath? It seems to be very useful tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '11, 03:37</strong></p>
<img src="https://secure.gravatar.com/avatar/45ba798692e5fef3a892f592fe74c9c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kisaa&#39;s gravatar image" />
<p><span>kisaa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kisaa has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8792" class="comments-container">
<span id="8841"></span>
<div id="comment-8841" class="comment">
<div id="post-8841-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Go ahead, if you like ;)</p>
</div>
<div id="comment-8841-info" class="comment-info">
<span class="comment-age">(05 Nov '11, 08:14)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-8792" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8792-form-container" class="comment-form-container">
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

