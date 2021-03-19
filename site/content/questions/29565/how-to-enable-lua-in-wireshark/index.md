+++
type = "question"
title = "How to enable LUA in wireshark ?"
description = '''This question is for Linux Centos Platform. I am doing a project in which Wireshark Traffic is to to be exported to a .pcap file and later used for further analysis. This Export is to be automatic that is programmatic. I found out that Wireshark process can be automated with LUA scripting Hence i do...'''
date = "2014-02-09T00:33:00Z"
lastmod = "2014-02-10T05:29:00Z"
weight = 29565
keywords = [ "lua", "tshark", "wireshark" ]
aliases = [ "/questions/29565" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to enable LUA in wireshark ?](/questions/29565/how-to-enable-lua-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29565-score" class="post-score" title="current number of votes">0</div><span id="post-29565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>This question is for Linux Centos Platform. I am doing a project in which Wireshark Traffic is to to be exported to a .pcap file and later used for further analysis. This Export is to be automatic that is programmatic. I found out that Wireshark process can be automated with LUA scripting Hence i download Wireshark but in the HELP or can say About Tab it displayed "Without LUA" so I am stuck up. I have searched a lot for a version of wireshark that supports LUA but no success. Can anyone put some light on this ?</p><p>There are basically 2 Problems ?</p><p>1.How to get a version of Wireshark with LUA ? Does it come bundled together ? OR I have to add it manually ? How to do so ?</p><p>2.Can Wireshark work on any other Language which can be used to automate entire wireshark Process ? I read tshark [command line version of wireshark] is the option but could not find any resources on it . Any help would be very useful.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '14, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/f55968049342e8ba14314f38df9ca9d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashish%20M&#39;s gravatar image" /><p><span>Ashish M</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashish M has no accepted answers">0%</span></p></div></div><div id="comments-container-29565" class="comments-container"><span id="29597"></span><div id="comment-29597" class="comment"><div id="post-29597-score" class="comment-score"></div><div class="comment-text"><p>How did you install it? Did you download the source and compile, or use Yum, or what? From source code (and possibly RPMs) Lua is only compiled in with a configure flag, as far as I know. On pre-built packaged Mac OS-X and Windows packages it's built in.</p></div><div id="comment-29597-info" class="comment-info"><span class="comment-age">(10 Feb '14, 00:36)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="29623"></span><div id="comment-29623" class="comment"><div id="post-29623-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I found out that Wireshark process can be automated with LUA scripting</p></blockquote><p>can you please add some information about the nature of the automation you need?</p></div><div id="comment-29623-info" class="comment-info"><span class="comment-age">(10 Feb '14, 05:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29565" class="comment-tools"></div><div class="clear"></div><div id="comment-29565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29598"></span>

<div id="answer-container-29598" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29598-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29598-score" class="post-score" title="current number of votes">3</div><span id="post-29598-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You said "traffic is to be exported to a .pcap file" and "export is to be automatic". Depending on how you mean those things, you may not need Lua, although Lua can export packets to pcap files. But if all you need is to start wireshark, capture traffic, and have it be saved to a pcap file... then use tshark instead. Tshark is the command-line version of wireshark. If you installed wireshark, then you have tshark as well. One of tshark's command-line options ('-w &lt;outfile&gt;') makes it write to a pcap file. So you can do all this "automating" with a shell script or alias.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29598" class="comments-container"><span id="29607"></span><div id="comment-29607" class="comment"><div id="post-29607-score" class="comment-score"></div><div class="comment-text"><p>Another option, if you can manage with only capture filters, is to use dumpcap that also comes along with Wireshark to make the captures and write them to a pcap file.</p><p>Dumpcap is a much lighter weight process to run for extended periods instead of tshark or wireshark.</p></div><div id="comment-29607-info" class="comment-info"><span class="comment-age">(10 Feb '14, 02:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-29598" class="comment-tools"></div><div class="clear"></div><div id="comment-29598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

