+++
type = "question"
title = "Detours removed"
description = '''Hi Everyone, I&#x27;ve just discovered that long-term detours around construction sites on the Q1 highway in Doha have been removed. I need help undoing the following changesets:   20169673   20171525   These edits appear to be made to reflect the old satellite images. Two large interchanges are being co...'''
date = "2014-09-04T16:02:00Z"
lastmod = "2014-09-04T19:59:00Z"
weight = 36598
keywords = [ "deleted", "undelete", "detour", "help" ]
aliases = [ "/questions/36598" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Detours removed](/questions/36598/detours-removed)

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
<span id="post-36598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36598-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Everyone,</p>
<p>I've just discovered that long-term detours around construction sites on the Q1 highway in Doha have been removed. I need help undoing the following changesets:</p>
<ul>
<li><h1 id="section">20169673</h1></li>
<li><h1 id="section-1">20171525</h1></li>
</ul>
<p>These edits appear to be made to reflect the old satellite images. Two large interchanges are being constructed in this area and the detours will be in place for at least another year. I have sent an email to the concerned user explaining the situation.</p>
<p>Thanks in advance, Shaun</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-deleted" rel="tag" title="see questions tagged &#39;deleted&#39;">deleted</span> <span class="post-tag tag-link-undelete" rel="tag" title="see questions tagged &#39;undelete&#39;">undelete</span> <span class="post-tag tag-link-detour" rel="tag" title="see questions tagged &#39;detour&#39;">detour</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '14, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e466cf295ae880686a4b809362f931b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rovingmedic&#39;s gravatar image" />
<p><span>rovingmedic</span><br />
<span class="score" title="1060 reputation points"><span>1.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rovingmedic has one accepted answer">5%</span></p>
</div>
</div>
<div id="comments-container-36598" class="comments-container">
&#10;</div>
<div id="comment-tools-36598" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36598-form-container" class="comment-form-container">
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

<span id="36615"></span>

<div id="answer-container-36615" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36615-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36615-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36615-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rovingmedic has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all - thanks for emailing the author of these changesets. It's not the first time that this particular user has made questionable edits like this. I'm sure that all edits were made in good faith - just that sometimes, they don't seem always particularly based in reality.</p>
<p>In order to get the old "detour" data back, you've got a few options:</p>
<p>1) If the changes had been recent, and the whole changeset is rubbish, then a complete changeset revert using <a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Reverter">JOSM's reverter plugin</a> would have been an option. As Simon says, normally 6-7 months is way too late for that - other people will have edited many of the ways since. In Qatar that may or may not be a problem - I'm not sure how much regular local mapping is going on.</p>
<p>2) Another JOSM option is the "<a href="http://wiki.openstreetmap.org/wiki/JOSM/Plugins/Undelete">undelete</a>" plugin. That requires that you find the numbers of the ways that have been deleted (and from looking at <a href="http://www.openstreetmap.org/changeset/20171525">this changeset</a> I'd guess that <a href="http://www.openstreetmap.org/way/256138077/history">this way</a> is one of them).</p>
<p>3) If you're not a regular JOSM user, then Potlatch 1's "undelete" option might be the easiest to use (I'll assume that <a href="http://www.openstreetmap.org/way/256138077/history">this way</a> is indeed the one to restore):</p>
<p>From the <a href="http://www.openstreetmap.org/way/256138077/history">history page for the way</a>, open a <a href="http://www.openstreetmap.org/node/2618315878">deleted node page</a> in another browser tab and select "view history".</p>
<p>That will show (in the previous version) the location that it was deleted from. Click that, and you'll be taken to that location in the map.</p>
<p>Select "edit with Potlatch 2". Edit the browser URL so that instead of something like</p>
<p><a href="http://www.openstreetmap.org/edit?editor=potlatch2#map=18/25.36404/51.44839">http://www.openstreetmap.org/edit?editor=potlatch2#map=18/25.36404/51.44839</a></p>
<p>you get</p>
<p><a href="http://www.openstreetmap.org/edit?editor=potlatch#map=18/25.36404/51.44839">http://www.openstreetmap.org/edit?editor=potlatch#map=18/25.36404/51.44839</a></p>
<p>(i.e. remove the "2" after "potlatch")</p>
<p>From the "Advanced" menu at the bottom select "Undelete" and wait a few seconds. You might get an error message, but ignore that - what you should see is some new bright red ways. Click on each of those in turn until you find the number (in this example 256138077) that you are looking for. Click "click to unlock" on the way and then immediately save.</p>
<p>Then edit the area in the normal way again using your normal editor - you'll see the undeleted way is back again, but you'll need to check it to make sure that it joins everything that it should.</p>
<p>4) One other option (mentioned only for completeness) is the perl <a href="http://wiki.openstreetmap.org/wiki/Revert_scripts">revert scripts</a> - but I wouldn't suggest trying that unless you've done it before.</p>
<p>Whatever method you end up using, it might be a good idea to ask in the #osm <a href="http://wiki.openstreetmap.org/wiki/Irc">IRC</a> channel (either for someone to help with the undelete, or to double-check what you've done)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '14, 19:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-36615" class="comments-container">
<span id="36616"></span>
<div id="comment-36616" class="comment">
<div id="post-36616-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the comprehensive reply. I'll have to spend some time studying the various options. I'll probably end up using JOSM (either a straight edit or one of the other techniques) as I can easily confirm arrangements with numerous gps tracks that I have of the area.</p>
</div>
<div id="comment-36616-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 19:59)</span> <span class="comment-user userinfo">rovingmedic</span>
</div>
</div>
</div>
<div id="comment-tools-36615" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36615-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="36602"></span>

<div id="answer-container-36602" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36602-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Both changesets are rather old (6-7 months) and the first one is quite large. With other words simply reverting the changesets is likely going to create a lot of conflicts and work unless you can clearly identify the changes/elements that need undoing/restoring. Alternatively: why not simply recreate the detour?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '14, 16:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-36602" class="comments-container">
<span id="36612"></span>
<div id="comment-36612" class="comment">
<div id="post-36612-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Simon, I was hoping not to have to redo all the changes. I haven't been able to see what the changesets include, but I'm basically only interested in the arrangements of the Q1 at the 2 locations near the IKEA store. The northern location involves the northbound lane and the on ramp while the southern location involves both lanes and on/off ramps. Unfortunately, I have been away from OSM for a while and only spotted this today.</p>
</div>
<div id="comment-36612-info" class="comment-info">
<span class="comment-age">(04 Sep '14, 18:25)</span> <span class="comment-user userinfo">rovingmedic</span>
</div>
</div>
</div>
<div id="comment-tools-36602" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36602-form-container" class="comment-form-container">
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

