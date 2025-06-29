+++
type = "question"
title = "One-way streets tagged with oneway = &quot;-1&quot; rendered incorrectly on Garmin"
description = '''Hi, I recently downloaded a map generated by http://garmin.openstreetmap.nl/. The data I downloaded was the map was of Ecuador, with the option &quot;Generic Routable (new style).&quot; The resulting map does have the direction tags rendered, however it seems like streets tagged with oneway using the &quot;-1&quot; opt...'''
date = "2015-02-17T23:14:00Z"
lastmod = "2015-02-19T08:07:00Z"
weight = 41095
keywords = [ "garmin.osm.nl", "bug" ]
aliases = [ "/questions/41095" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [One-way streets tagged with oneway = "-1" rendered incorrectly on Garmin](/questions/41095/one-way-streets-tagged-with-oneway-1-rendered-incorrectly-on-garmin)

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
<span id="post-41095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41095-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I recently downloaded a map generated by <a href="http://garmin.openstreetmap.nl/">http://garmin.openstreetmap.nl/</a>. The data I downloaded was the map was of Ecuador, with the option "Generic Routable (new style)." The resulting map does have the direction tags rendered, however it seems like streets tagged with oneway using the "-1" option to switch the directionality have arrows pointing the wrong way on <a href="https://www.evernote.com/shard/s73/sh/27ad85ad-bcfb-497b-9b9e-51b08aaf7456/cd5c3f6b7386a6c6c86eb23185cace3a/deep/0/Screenshot-2-17-15,-6-10-PM.png">Basecamp</a> and my Garmin GPS. <a href="https://www.evernote.com/shard/s73/sh/59189fef-ed57-44e5-b309-b3106ec63d72/3f56e2fbfdc3d2727fb886698897ca9f/deep/0/Java_OpenStreetMap_Editor.png">JOSM in these cases points the correct way</a>, as does the <a href="https://www.openstreetmap.org/way/160695136#map=19/-0.20265/-78.49515">openstreetmap web site</a>.</p>
<p>I'd be happy to try to make a contribution (code or data), but does anyone have a pointer to where this may be occurring? If this isn't the best place to report this kind of issue, I'd appreciate a pointer to the correct bug tracking system.</p>
<p>Thanks,</p>
<p>Justin</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-garmin.osm.nl" rel="tag" title="see questions tagged &#39;garmin.osm.nl&#39;">garmin.osm.nl</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '15, 23:14</strong></p>
<img src="https://secure.gravatar.com/avatar/dc13eb3fe110b6ea822adbc797ba0454?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jsl&#39;s gravatar image" />
<p><span>jsl</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jsl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41095" class="comments-container">
&#10;</div>
<div id="comment-tools-41095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41095-form-container" class="comment-form-container">
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

<span id="41096"></span>

<div id="answer-container-41096" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41096-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-41096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jsl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>oneway=-1</span> is a correct/<a href="https://taginfo.openstreetmap.org/keys/?key=oneway#values">not seldom</a> tagging, so any Garmin map should be able to work with this (although this might involve a bit of programming in the map creation process which may simply not be done yet, but I doubt it).</p>
<p>First check that the OSM data is right (which you seem to have done already). Afterwards you may want to contact the creator of the garmin.openstreetmap.nl map. You find contact data in the left menu there. As far as I know using the linked forum thread is best (the map creator is active there).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '15, 23:25</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '15, 23:54</strong> </span></p>
</div>
</div>
<div id="comments-container-41096" class="comments-container">
<span id="41102"></span>
<div id="comment-41102" class="comment">
<div id="post-41102-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thanks <a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>. I've done a bit more research and <a href="http://forum.openstreetmap.org/viewtopic.php?pid=486521#p486521">posted to the forum for</a> <a href="http://garmin.openstreetmap.nl/">http://garmin.openstreetmap.nl/</a>. FYI, it seems it's probably just an incorrect style being applied, as indicated on the <a href="http://www.mkgmap.org.uk/pipermail/mkgmap-dev/2014q1/019681.html">mkgmap-dev list</a>.</p>
</div>
<div id="comment-41102-info" class="comment-info">
<span class="comment-age">(18 Feb '15, 08:38)</span> <span class="comment-user userinfo">jsl</span>
</div>
</div>
<span id="41130"></span>
<div id="comment-41130" class="comment">
<div id="post-41130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That said, about the only time I can think of using oneway=-1 myself was for some bizarre alleyway next to the railroad tracks and State Street in Salem, Oregon where a few modes were one way in one direction, a mode or two could go both ways, and the default signed was the direction opposite the majority of traffic's flow. I honestly can't think of any situation where oneway=-1 doesn't involve an exceptionally convoluted ground truth.</p>
<p>Definitely a bug in the navigation toolchain for you. Probably also a tagging bug.</p>
</div>
<div id="comment-41130-info" class="comment-info">
<span class="comment-age">(18 Feb '15, 20:12)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="41136"></span>
<div id="comment-41136" class="comment">
<div id="post-41136-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can avoid the oneway=-1 issue by reversing the draw direction of a way before applying the oneway tag. oneway=-1 is only invoked when the direction of travel is in the opposite direction from the draw direction.</p>
<p>The tag is so confusing to me that I'll sometimes delete it, reverse the way by typing R, then reapply the oneway tag.</p>
</div>
<div id="comment-41136-info" class="comment-info">
<span class="comment-age">(18 Feb '15, 23:53)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="41138"></span>
<div id="comment-41138" class="comment">
<div id="post-41138-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave"></a><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>: whyever you are deleting the tag just to re-add it later … but check that no other tag/relation refers to the way's direction when reversing a way (if your editor doesn't do that for you)! Yes, <code>oneway=yes</code> is nicer and should be used, if possible without unnecessary edits (e.g. when creating new ways).</p>
</div>
<div id="comment-41138-info" class="comment-info">
<span class="comment-age">(19 Feb '15, 00:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="41139"></span>
<div id="comment-41139" class="comment">
<div id="post-41139-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I would never change a pre existing oneway=-1 tag. I only use the method I described when adding new stuff to OSM.</p>
</div>
<div id="comment-41139-info" class="comment-info">
<span class="comment-age">(19 Feb '15, 01:29)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="41140"></span>
<div id="comment-41140" class="comment not_top_scorer">
<div id="post-41140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5016/alaskadave"></a><a href="https://help.openstreetmap.org/users/5016/alaskadave">@AlaskaDave</a>: Ah, sorry, it was not clear to me that you were talking about new ways, thanks!</p>
</div>
<div id="comment-41140-info" class="comment-info">
<span class="comment-age">(19 Feb '15, 01:58)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41096" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-41096-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41143"></span>

<div id="answer-container-41143" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41143-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41143-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41143-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is fixed in the style of the Generic new OSM maps, thanks for reporting Justin!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '15, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-41143" class="comments-container">
&#10;</div>
<div id="comment-tools-41143" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41143-form-container" class="comment-form-container">
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

