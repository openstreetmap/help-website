+++
type = "question"
title = "[closed] conflict editor in iD is bogous"
description = '''when there are edit conflicts in iD the conflict editors does not help solving them:  - it proposes to download our changes, but the link provided goes to a blank page.  - trying to select any propposed edit from the change fails, iD does not properly download all the needed changes. Then continuing...'''
date = "2017-09-18T20:30:00Z"
lastmod = "2017-09-18T23:08:00Z"
weight = 59678
keywords = [ "conflicts", "ideditor", "bugs" ]
aliases = [ "/questions/59678" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] conflict editor in iD is bogous](/questions/59678/conflict-editor-in-id-is-bogous)

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
<span id="post-59678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59678-score" class="post-score" title="current number of votes">
-7
</div>
<span id="post-59678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>when there are edit conflicts in iD the conflict editors does not help solving them: - it proposes to download our changes, but the link provided goes to a blank page. - trying to select any propposed edit from the change fails, iD does not properly download all the needed changes. Then continuing will fail because iD still wants to save objects from their old version iD</p>
<p>In summary, iD is unusable for editing in areas where there are other users cooperating, we just loose ALL our edits for a single object change that we cannot refresh to download them in their current version so that we can then update them as needed.</p>
<p>The conflict editor simply DOES NOT work at all !</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-conflicts" rel="tag" title="see questions tagged &#39;conflicts&#39;">conflicts</span> <span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-bugs" rel="tag" title="see questions tagged &#39;bugs&#39;">bugs</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Sep '17, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '17, 17:20</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-59678" class="comments-container">
<span id="59679"></span>
<div id="comment-59679" class="comment">
<div id="post-59679-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd suggest that you create an issue (or update an existing one) over at <a href="https://github.com/openstreetmap/iD/issues">https://github.com/openstreetmap/iD/issues</a> . The OSM help site isn't really the place for "X doesn't work" statements - it's not a "question" that anyone can answer.</p>
<p>What I would suggest is that you explain the problem with a series of steps to reproduce - if you do that on the dev server <a href="https://master.apis.dev.openstreetmap.org/">https://master.apis.dev.openstreetmap.org/</a> then you can create any test data that you like.</p>
</div>
<div id="comment-59679-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 20:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="59680"></span>
<div id="comment-59680" class="comment">
<div id="post-59680-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hey verdy_p, the issue with the broken "download changes" link is something I just learned about last week. Turns out that recent versions of Chrome and other browsers no longer like linking to <code>data:</code> urls.<br />
<a href="https://github.com/openstreetmap/iD/issues/4346">https://github.com/openstreetmap/iD/issues/4346</a></p>
<p>I worked on it over the weekend and was able to fix the issue so that now downloading changes will work again in all supported browsers on the Conflict Resolution screen, as well as the general Upload Changes screen. <a href="https://github.com/openstreetmap/iD/pull/4350">https://github.com/openstreetmap/iD/pull/4350</a></p>
<p>I'll probably release a new version of iD in the next few days that includes this fix. Thanks for your understanding!</p>
</div>
<div id="comment-59680-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 20:50)</span> <span class="comment-user userinfo">bhousel</span>
</div>
</div>
<span id="59683"></span>
<div id="comment-59683" class="comment">
<div id="post-59683-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Closed with "negative" comment, but this is a REAL problem.</p>
<p>I've never been able to use the conflict editor in iD, it ALWAYS fails finally when all conflicts are supposed to be solved, by a fatal error where iD contains the wrong old version.</p>
<p>It's even impossible to just discard changes on conflicting objetct and continue with others (there may be plenty of them and loosing everything is definitely not an option when we can simply not even download these changes for external review, for example as an .odm file we could fix by using JOSM instead).</p>
<p>So YES this question is FULLY RELEVANT and ON TOPIC, <a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> you are compeltely wrong ! And it concerns lots of people (not just me).</p>
<p>This is really a severe bug. And it is extremely easy to reproduce, by using two distinct browsers connected to different users and user1 making a change to a way currently loaded by User2, then User1 commiting changes on one node, before User2 attempts to commit changes to the same way (such as adding or moving the same node).</p>
<p>Please REOPEN this unsolved bug</p>
</div>
<div id="comment-59683-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 21:29)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="59685"></span>
<div id="comment-59685" class="comment">
<div id="post-59685-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"Closed with "negative" comment, but this is a REAL problem."</p>
<p>Your "question" has not been closed. I don't know where you're seeing this.</p>
<p>"So YES this question is FULLY RELEVANT and ON TOPIC, <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> you are compeltely wrong ! And it concerns lots of people (not just me)."</p>
<p>As SomeoneElse said, this is a Q&amp;A site. Someone asks how to do something, and others give answers to help do that thing. What exactly is your question? If you don't have one, then the best place to post your comments about this issue with iD is in GitHub.</p>
</div>
<div id="comment-59685-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 21:40)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="59686"></span>
<div id="comment-59686" class="comment not_top_scorer">
<div id="post-59686-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>This real bug has been reported elsewhere and accepted, for example <a href="/questions/31318/how-do-i-find-a-way-by-id-in-id-to-fix-version-mismatch-and-then-save-my-edit">https://help.openstreetmap.org/questions/31318/how-do-i-find-a-way-by-id-in-id-to-fix-version-mismatch-and-then-save-my-edit</a></p>
</div>
<div id="comment-59686-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 21:42)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="59687"></span>
<div id="comment-59687" class="comment not_top_scorer">
<div id="post-59687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1555/verdy_p">@Verdy_p</a> - Did you actually read bhousel's comment above?</p>
</div>
<div id="comment-59687-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 21:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="59689"></span>
<div id="comment-59689" class="comment not_top_scorer">
<div id="post-59689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes of course I read it. You just refuse to admit this is a bug, but many users complain about this. The bug is not solved currently. You refused the bug but bhousel saw it as a real bug on which he is working. Don't be surprised that people stop working on HOT projects when most of them use iD, and if they have passed long time draxing things and thne connecting their ways, to surrounding tile, and loose everything because they can't pass through the edit conflict, they will stop contributing because of their lost patient editing time.</p>
</div>
<div id="comment-59689-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 22:25)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="59692"></span>
<div id="comment-59692" class="comment not_top_scorer">
<div id="post-59692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>SomeoneElse isn't refusing to admit there's a bug. He's just telling you that this isn't the appropriate place to be discussing it. I ask again, what is your question for this Q&amp;A site?</p>
</div>
<div id="comment-59692-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 22:41)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="59693"></span>
<div id="comment-59693" class="comment">
<div id="post-59693-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/1555/verdy_p"></a><a href="https://help.openstreetmap.org/users/1555/verdy_p">@verdy_p</a> the help site is not a general discussion forum, nor an issue tracker for bug reports. Please take your non-stop arguments elsewhere.</p>
</div>
<div id="comment-59693-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 22:42)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="59696"></span>
<div id="comment-59696" class="comment not_top_scorer">
<div id="post-59696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you cannot see the question, which is there... I have to repeat it, because you don't read: how do we connect then and mange the local profiles? It's impossible. I see your constant replies here very agressive what what is a real problem without solution for now.</p>
</div>
<div id="comment-59696-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 23:08)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-59678" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-59678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Too subjective and argumentative" by SimonPoole 18 Sep '17, 22:48

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59684"></span>

<div id="answer-container-59684" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59684-score" class="post-score" title="current number of votes">
-7
</div>
<span id="post-59684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I will NOT vote up for the speedy "solution" proposed incorrectly by Someone else, I would vote down if it was possible, as it is really incorrect.</p>
<p>And this is not about "testing" things, but real edits in the main database (so the dev database in your suggestion is compeltely irrelevant)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '17, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '17, 21:39</strong> </span></p>
</div>
</div>
<div id="comments-container-59684" class="comments-container">
<span id="59694"></span>
<div id="comment-59694" class="comment">
<div id="post-59694-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please stop misusing the help site, in particular stop posting comments as answers.</p>
</div>
<div id="comment-59694-info" class="comment-info">
<span class="comment-age">(18 Sep '17, 22:45)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-59684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59684-form-container" class="comment-form-container">
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

