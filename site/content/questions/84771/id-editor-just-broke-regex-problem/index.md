+++
type = "question"
title = "[closed] iD editor just broke: regex problem"
description = '''Sometime between 1 - 2 months ago when I last edited and now, the in-browser editor has been rendered nonfunctional for me. The problem I can dig up in the debugger reads thusly:  SyntaxError: invalid regular expression flag s  id-6172ebd02911868e7b330b540a9baa13d0fcf18c6f57ad447234ca1ec33f4e0f.js:1...'''
date = "2022-06-15T01:13:00Z"
lastmod = "2022-06-19T13:16:00Z"
weight = 84771
keywords = [ "regex", "javascript" ]
aliases = [ "/questions/84771" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] iD editor just broke: regex problem](/questions/84771/id-editor-just-broke-regex-problem)

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
<span id="post-84771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84771-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-84771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sometime between 1 - 2 months ago when I last edited and now, the in-browser editor has been rendered nonfunctional for me. The problem I can dig up in the debugger reads thusly:</p>
<pre><code>   SyntaxError: invalid regular expression flag s
   id-6172ebd02911868e7b330b540a9baa13d0fcf18c6f57ad447234ca1ec33f4e0f.js:11:8250</code></pre>
in file<br />
<a href="https://www.openstreetmap.org/assets/id-6172ebd02911868e7b330b540a9baa13d0fcf18c6f57ad447234ca1ec33f4e0f.js,">https://www.openstreetmap.org/assets/id-6172ebd02911868e7b330b540a9baa13d0fcf18c6f57ad447234ca1ec33f4e0f.js,</a><br />
the code fragment in question reads
<pre><code>   {var n=o.replace(/#.*/us,&quot;&quot;);</code></pre>
"s" is a rather recent regex modifier, and is NOT guaranteed to be present in some number of even recent-ish vintage browsers. It's not even shown at regex101.com yet, a very common go-to reference. This <strong>gratuitous</strong> type of change has probably broken functionality for a lot of people, who are perhaps not at liberty to rip up their whole browser environment for a bleeding-edge upgrade they don't need. Your "because it's new-n-shiny" is our pain in the ass, sorry.
<p>The workaround for the functionality of the "s" flag is to use '[\s\S]' instead of '.', then matching works across newlines. Someone should FIX this, if they care about keeping the community accomodating and welcome. Coming home from an afternoon of mapping trails that aren't in the database yet, being blocked from adding them is not exactly what I expected.</p>
<p>How does one actually contact the OSM developers, so stuff like this gets in front of the right eyeballs?</p>
<p>_H*</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-regex" rel="tag" title="see questions tagged &#39;regex&#39;">regex</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '22, 01:13</strong></p>
<img src="https://secure.gravatar.com/avatar/3031665c506b04f416a1af103cf8cf6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Hobbit&#39;s gravatar image" />
<p><span>_Hobbit</span><br />
<span class="score" title="51 reputation points">51</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Hobbit has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 Jun '22, 22:14</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-84771" class="comments-container">
<span id="84776"></span>
<div id="comment-84776" class="comment">
<div id="post-84776-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which actual browser are you seeing this problem with? You've said "some number of even recent-ish vintage browsers" but that makes literally no sense.</p>
</div>
<div id="comment-84776-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 14:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84786"></span>
<div id="comment-84786" class="comment">
<div id="post-84786-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://github.com/openstreetmap/iD/pull/9165">https://github.com/openstreetmap/iD/pull/9165</a></p>
<p>'nuff said</p>
<p>_H*</p>
</div>
<div id="comment-84786-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 23:45)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
</div>
<div id="comment-tools-84771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84771-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Other" by SimonPoole 21 Jun '22, 22:14

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="84772"></span>

<div id="answer-container-84772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84772-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-84772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://github.com/openstreetmap/iD/issues">https://github.com/openstreetmap/iD/issues</a> is the place. Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '22, 06:00</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-84772" class="comments-container">
<span id="84774"></span>
<div id="comment-84774" class="comment">
<div id="post-84774-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... which requires a Github account. It's bad enough I have to do browser calisthenics to even log in to THIS and post, now you're making the assumption that I'm on github and/or have to create <strong>yet another</strong> username and password just to get anywhere near receiving support.</p>
<p>Thanks, I suppose. You realize that this illustrates another part of the larger problem, right?</p>
<p>_H*</p>
</div>
<div id="comment-84774-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 14:23)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="84775"></span>
<div id="comment-84775" class="comment">
<div id="post-84775-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21890/_hobbit">@_hobbit</a> you can dislike the fact that iD is developed at Github, but you can't complain that the answer is incorrect :)</p>
<p>What would you prefer - that OSM developers spent time on an in-house software development platform rather than use something external?</p>
</div>
<div id="comment-84775-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 14:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84777"></span>
<div id="comment-84777" class="comment">
<div id="post-84777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21890/_hobbit">@_hobbit</a> Get a passwort manager such as KeePassXC.</p>
</div>
<div id="comment-84777-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 14:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="84779"></span>
<div id="comment-84779" class="comment not_top_scorer">
<div id="post-84779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I appreciate the open-source nature of iD and OSM components are open-source, and I don't care where it is developed, but forcing me to chase them over there to have any hope of opening a useful support case is still disingenuous. Personally, I actually do have a github account [very disused], I have a password manager, I have different vintages of browsers to test things under, but how does that help the next person who doesn't have those resources, but still has a problem with iD or any other piece? Not every OSM user is even close to having or wanting developer or power-user style tools, so please think about the larger community.</p>
<p>There is NO mention of any of this on the main OSM website, no procedure to actually report a bug or problem given, just vague hints under "help" about forums and wikis and IRC and off-topic email lists, that don't lead directly to solutions either. That area is in sad need of a refresh, really. And various other comments I've read support that.</p>
<p>Nobody even offered to simply <strong>forward</strong> my issue <strong>TO</strong> the people on github, or acknowledged that maybe there should be a bug submission input means on or linked to from the main site. Instead, I get this runaround. Other than h_mlet's pointer, as indirect as it might be, this is not a good look to someone starting from ground zero.</p>
<p>_H*</p>
</div>
<div id="comment-84779-info" class="comment-info">
<span class="comment-age">(15 Jun '22, 18:30)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="84800"></span>
<div id="comment-84800" class="comment">
<div id="post-84800-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Forwarding other people's bug reports always has the problem that the developers cannot request further details if they cannot reproduce the problem. In addition, the original reporter never receives a response when the problem is fixed and does not receive information about possible workarounds.</p>
</div>
<div id="comment-84800-info" class="comment-info">
<span class="comment-age">(16 Jun '22, 15:48)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="84818"></span>
<div id="comment-84818" class="comment">
<div id="post-84818-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Carefully avoiding any mention of which version of the Pine browser you are running discourages any possibility of anyone taking the initiative of forwarding this issue to Github for you.</p>
</div>
<div id="comment-84818-info" class="comment-info">
<span class="comment-age">(19 Jun '22, 13:16)</span> <span class="comment-user userinfo">Mike N</span>
</div>
</div>
</div>
<div id="comment-tools-84772" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-84772-form-container" class="comment-form-container">
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

