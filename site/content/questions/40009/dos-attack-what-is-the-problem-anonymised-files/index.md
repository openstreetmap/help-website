+++
type = "question"
title = "Dos attack? What is the problem? + anonymised files."
description = '''Hey communety, I have some problems with my internet connection and I think somebody is using an &quot;ip stresser&quot; to disconnect me from the internet. I captured using wireshark some package and ask somebody to look at it.  The files (3) are anonymised using tracewrangler and uplouded to dropbox. https:...'''
date = "2015-02-21T13:34:00Z"
lastmod = "2015-02-23T09:20:00Z"
weight = 40009
keywords = [ "dos", "ddos", "problem", "internet" ]
aliases = [ "/questions/40009" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dos attack? What is the problem? + anonymised files.](/questions/40009/dos-attack-what-is-the-problem-anonymised-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40009-score" class="post-score" title="current number of votes">0</div><span id="post-40009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey communety,</p><p>I have some problems with my internet connection and I think somebody is using an "ip stresser" to disconnect me from the internet. I captured using wireshark some package and ask somebody to look at it.</p><p>The files (3) are anonymised using tracewrangler and uplouded to dropbox. <a href="https://www.dropbox.com/sh/cs3wlpwqp5tlftd/AACh9Lrcbe_BntWkDXbZ8srja?dl=0">https://www.dropbox.com/sh/cs3wlpwqp5tlftd/AACh9Lrcbe_BntWkDXbZ8srja?dl=0</a></p><p>thanks in advanced You are the best :)</p><p>Gr, JP</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dos" rel="tag" title="see questions tagged &#39;dos&#39;">dos</span> <span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-internet" rel="tag" title="see questions tagged &#39;internet&#39;">internet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Feb '15, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/e16acb9f62993f25fc59c1cf66ebd284?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jplwolters&#39;s gravatar image" /><p><span>jplwolters</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jplwolters has no accepted answers">0%</span></p></div></div><div id="comments-container-40009" class="comments-container"></div><div id="comment-tools-40009" class="comment-tools"></div><div class="clear"></div><div id="comment-40009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40028"></span>

<div id="answer-container-40028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40028-score" class="post-score" title="current number of votes">0</div><span id="post-40028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Apparently you captured on your local network. You won't be able to see and "ip stresser" (what is that?) traffic if a bad guy is really hammering your link, because your firewall/router will drop it, so you won't see that traffic on the local network.</p><p>There are no (obvious) signs for any kind of DoS attack. There are a some TCP RESETS, but all from your internal clients and by far less than TCP SYN. The only strange thing is that you are using a lot of high ports to connect to servers on the internet. That could be gaming traffic. Due to the use of an anonymizer it's not possible to analyze that any further.</p><p>Therefore, without more information, it's impossible to give any meaningful answer.</p><p>So, why do you believe you are being disconnected from the internet?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '15, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40028" class="comments-container"></div><div id="comment-tools-40028" class="comment-tools"></div><div class="clear"></div><div id="comment-40028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

