+++
type = "question"
title = "[closed] drop down menus in JOSM are hard to keep open with the mouse"
description = '''I am running JOSM 6238 on openSUSE 12.3 (x86_64) with IcedTea 2.4.1. Since I switched to openSUSE from an Ubuntu derivative, I have had problems with the drop down menus in JOSM. When I click to open them I am force to move my cursor some distance off the menu to keep them open. I must move even fur...'''
date = "2013-10-14T02:44:00Z"
lastmod = "2013-10-15T04:05:00Z"
weight = 27133
keywords = [ "drop_down_menus", "josm", "openjdk", "bug" ]
aliases = [ "/questions/27133" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] drop down menus in JOSM are hard to keep open with the mouse](/questions/27133/drop-down-menus-in-josm-are-hard-to-keep-open-with-the-mouse)

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
<span id="post-27133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27133-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am running JOSM 6238 on openSUSE 12.3 (x86_64) with IcedTea 2.4.1. Since I switched to openSUSE from an Ubuntu derivative, I have had problems with the drop down menus in JOSM. When I click to open them I am force to move my cursor some distance off the menu to keep them open. I must move even further to the right if I wish to open sub-menus. What is going on?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-drop_down_menus" rel="tag" title="see questions tagged &#39;drop_down_menus&#39;">drop_down_menus</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-openjdk" rel="tag" title="see questions tagged &#39;openjdk&#39;">openjdk</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Oct '13, 02:44</strong></p>
<img src="https://secure.gravatar.com/avatar/bf25a8b2b0865086f73a82428176a6ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sammuell&#39;s gravatar image" />
<p><span>sammuell</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sammuell has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Oct '13, 04:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-27133" class="comments-container">
<span id="27137"></span>
<div id="comment-27137" class="comment">
<div id="post-27137-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Do you have similar problems with other Java applications? I think it would be the best to create a ticket at <a href="http://josm.openstreetmap.de/newticket">josm.openstreetmap.de</a>. You can log in using your regular OSM account.</p>
</div>
<div id="comment-27137-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 07:29)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27144"></span>
<div id="comment-27144" class="comment not_top_scorer">
<div id="post-27144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds like a problem with your java distribution. Try to update to the latest Java or install Oracle/Sun Java instead of OpenJava. Also give a try with 32 vs 64 bits. My 2 cents.</p>
</div>
<div id="comment-27144-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 12:04)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="27145"></span>
<div id="comment-27145" class="comment">
<div id="post-27145-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><span></span><span>@Pieren</span> There is no easy way to install the official Oracle Java 7 on Linux due to Oracles braindead policy. OpenJDK/IcedTea is a valid alternative, usually runs without problems and is shipped by almost all Linux distributions. Hence switching is not a valid solution, and if it is a problem with this specific runtime then many other users would be affected, too.</p>
</div>
<div id="comment-27145-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 12:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27147"></span>
<div id="comment-27147" class="comment not_top_scorer">
<div id="post-27147-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I received similar complains about my JOSM plugin and all of them have been solved by changing the java engine.</p>
</div>
<div id="comment-27147-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 13:26)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="27148"></span>
<div id="comment-27148" class="comment">
<div id="post-27148-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>no menu problem as you describe with JOSM 6238 with OpenJDK (32 bit) for me. However, please report that issue at the JOSM ticket system for further investigation. JOSM really <em>should</em> run with OpenJDK.</p>
</div>
<div id="comment-27148-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 14:00)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="27167"></span>
<div id="comment-27167" class="comment">
<div id="post-27167-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@Scai</span> <span></span><span>@aseerel4c26</span> I installed OpenJUMP to compare, and experienced a similar problem. Should I open a JOSM ticket if it appears to be an OpenJDK problem?</p>
</div>
<div id="comment-27167-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 19:08)</span> <span class="comment-user userinfo">sammuell</span>
</div>
</div>
<span id="27175"></span>
<div id="comment-27175" class="comment not_top_scorer">
<div id="post-27175-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@sammuell</span>: Well, if you really think it is not a problem of the programs but of the Java machine, then you could file a bug directly <a href="http://openjdk.java.net/contribute/">there</a> (somehow, somewhere). But I think it is better to file a bug for JOSM first. Maybe it is also no bug in OpenJDK but just a bit non-standard-conformance by JOSM and OpenJUMP. Anyhow, link this discussion and try to describe the problem in a way which makes it reproducible. You also may mention a link to the bug report here.</p>
</div>
<div id="comment-27175-info" class="comment-info">
<span class="comment-age">(14 Oct '13, 21:29)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="27179"></span>
<div id="comment-27179" class="comment">
<div id="post-27179-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Ticket has been submitted. <a href="http://josm.openstreetmap.de/ticket/9193">http://josm.openstreetmap.de/ticket/9193</a></p>
</div>
<div id="comment-27179-info" class="comment-info">
<span class="comment-age">(15 Oct '13, 04:05)</span> <span class="comment-user userinfo">sammuell</span>
</div>
</div>
</div>
<div id="comment-tools-27133" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-27133-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "This specific issue is at a bugtracker now (see link in the last comment)." by aseerel4c26 15 Oct '13, 04:23

</div>

</div>

</div>

