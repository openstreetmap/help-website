+++
type = "question"
title = "Tshark: Cannot run Dissector() while using option &quot;-w&quot;"
description = '''Hi all, i&#x27;m using tshark command and trying some scenarios but something seems to be strange. I modified the Dissectors() function. here is my concern:  **tshark -i 5**  And the program went through my code in Dissectors() but it wrote a large tmp file. So, what happens if I remove the tmp file? I t...'''
date = "2013-10-06T21:54:00Z"
lastmod = "2013-10-07T00:56:00Z"
weight = 25690
keywords = [ "dissector", "tshark", "dumpcap" ]
aliases = [ "/questions/25690" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark: Cannot run Dissector() while using option "-w"](/questions/25690/tshark-cannot-run-dissector-while-using-option-w)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25690-score" class="post-score" title="current number of votes">0</div><span id="post-25690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, i'm using tshark command and trying some scenarios but something seems to be strange. I modified the Dissectors() function. here is my concern:</p><ol><li><code>**tshark -i 5**</code></li></ol><p>And the program went through my code in Dissectors() but it wrote a large tmp file. So, what happens if I remove the tmp file? I tried but nothing happened, the program still print out anything without tmp file. So, how does the program have data to dissect because previously, i ever though dumpcap write data to tmp file then Dissectors() read data from tmp file to dissect but now after removing this file, Dissectors() was still working. if so, why we need a large tmp file while after removing, nothing change? Please correct me if i said something wrong.</p><ol><li><code>**tshark -i 5 -w /tmp/sonnh.pcap**</code></li></ol><p>When I use option "-w" , nothing went through my code in Dissectors(), so I think if I use "-w", the program <strong>only</strong> call dumpcap <strong>without</strong> (or <strong>skip</strong>) calling Dissectors(), is it right? Other evidence which made me think it could be right is that there is no any value or data print out when I use "-w". Also, we cannot use filter together with "-w", simply because of no Dissector()called if we are using "-w". am I right?</p><ol><li>I want to run my code in Dissectors() by using tshark but don't want to keep a larger tmp file. So, anything wrong if I try to insert code into Dissector to remove a tmp file? (because i cannot run my code when I use option "-w" to solve the problem of large tmp file) Thanks so much.</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div></div><div id="comments-container-25690" class="comments-container"></div><div id="comment-tools-25690" class="comment-tools"></div><div class="clear"></div><div id="comment-25690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25692"></span>

<div id="answer-container-25692" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25692-score" class="post-score" title="current number of votes">1</div><span id="post-25692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you run with <code>-w</code> and without <code>-P</code>, tshark writes the raw packet data to the file specified with <code>-w</code> and does <em>not</em> dissect packets.</p><p>If you want the raw packet data to be written to a file <em>and</em> have the packets dissected, use the <code>-P</code> flag and, if you want the a detailed dissection, the <code>-V</code> flag in addition to the <code>-P</code> flag.</p><p>If you <em>only</em> want the packets to be dissected, and <em>don't</em> want the raw packet data to be written to a file, don't use the <code>-w</code> flag.</p><p>(This is similar to tcpdump, which dissects packets if you don't give it the <code>-w</code> flag, and writes them to a file without dissecting them if you give it the <code>-w</code> flag.)</p><p>Currently, tshark writes captured packets to a temporary file in <em>all</em> cases, even if you <em>don't</em> specify <code>-w</code>. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2743">Bug 2343</a> requests that it not do so, but that bug isn't fixed yet, so you currently cannot run tshark, have it capture packet data, and not write a temporary file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '13, 23:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-25692" class="comments-container"><span id="25695"></span><div id="comment-25695" class="comment"><div id="post-25695-score" class="comment-score"></div><div class="comment-text"><p>Thanks Harris, I understand that we always have a temp file, but I just want to delete it due to disk space because my program run in real and it is non-stop. With the option -P and -W, now i can go through the Dissectors and also able to auto delete the temp file. Thanks for your comment. But i just wonder why tshark needs a temp file? I tried to remove temp file and see nothing happened with tshark.</p></div><div id="comment-25695-info" class="comment-info"><span class="comment-age">(07 Oct '13, 00:15)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="25701"></span><div id="comment-25701" class="comment"><div id="post-25701-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>But i just wonder why tshark needs a temp file?</p></blockquote><p>Because there needs to be <em>some</em> way for dumpcap to supply it with packets, and because the protocol between dumpcap and tshark would need to be different if it were supplying it with packets over a pipe rather than in a file, and we haven't gotten around to making that work yet.</p><blockquote><p>I tried to remove temp file and see nothing happened with tshark.</p></blockquote><p>If this is on UN*X (Linux, OS X, *BSD, Solaris, etc.), then removing a file that some process has open just removes its name from a directory; the file doesn't disappear until the last file that has it open closes it, and both dumpcap and tcpdump have it open. It still takes up space while it's still around.</p></div><div id="comment-25701-info" class="comment-info"><span class="comment-age">(07 Oct '13, 00:56)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-25692" class="comment-tools"></div><div class="clear"></div><div id="comment-25692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

