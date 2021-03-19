+++
type = "question"
title = "Easy way to save tcp streams?"
description = '''If I have a trace with say 20 tcp streams, is there an easy way to save out each tcp stream to its own separate file, whether it be using tshark, editcap, gui, etc.? Or is the only way to do this to use a display filter for each stream and save as one by one? Thanks!'''
date = "2011-06-22T13:35:00Z"
lastmod = "2012-12-25T03:59:00Z"
weight = 4677
keywords = [ "save" ]
aliases = [ "/questions/4677" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Easy way to save tcp streams?](/questions/4677/easy-way-to-save-tcp-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4677-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>If I have a trace with say 20 tcp streams, is there an easy way to save out each tcp stream to its own separate file, whether it be using tshark, editcap, gui, etc.? Or is the only way to do this to use a display filter for each stream and save as one by one?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">save</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/98ec75d031a962cf9b8cd542330f511d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seyerekim&#39;s gravatar image" /><p>seyerekim<br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seyerekim has no accepted answers">0%</span></p></div></div><div id="comments-container-4677" class="comments-container"></div><div id="comment-tools-4677" class="comment-tools"></div><div class="clear"></div><div id="comment-4677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4681"></span>

<div id="answer-container-4681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4681-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to split the file into separate files in pcap format, each containing one tcp stream, you can do that with a little scripting around tshark. If you are only interested in the tcp payload of each stream, you'd have to use a tool like "tcpflow".</p><p>Assuming the first, you can do this by the following (just an example):</p><pre><code>for stream in `tshark -r &lt;pcapfile&gt; -T fields -e tcp.stream | sort -n | uniq`
do
    echo $stream
    tshark -r &lt;pcapfile&gt; -w stream-$stream.cap -R &quot;tcp.stream==$stream&quot;
done</code></pre><p>(You can also just do a for loop to the highest tcp.stream number, but there may be gaps in the tcp.stream numbering as it reuses the conversation index and there may be other conversations than tcp)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '11, 15:47</p></div></div><div id="comments-container-4681" class="comments-container"><span id="4686"></span><div id="comment-4686" class="comment"><div id="post-4686-score" class="comment-score"></div><div class="comment-text"><p>Thanks Sake, this helps!</p></div><div id="comment-4686-info" class="comment-info"><span class="comment-age">(22 Jun '11, 19:54)</span> seyerekim</div></div><span id="24250"></span><div id="comment-24250" class="comment"><div id="post-24250-score" class="comment-score"></div><div class="comment-text"><p>FYI, on Windows using cygwin, you may need to pipe the output of <code>uniq</code> to <code>sed</code> to remove the extraneous carriage return; otherwise you may see an <em>invalid address:port pair</em> error message, i.e.:</p><pre><code>for stream in `tshark -r &lt;pcapfile&gt; -T fields -e tcp.stream | sort -n | uniq | sed &#39;s/\r//&#39;`</code></pre><p>See also <a href="http://ask.wireshark.org/questions/24207/invalid-addressport-pair">this</a> question and my answer there.</p></div><div id="comment-24250-info" class="comment-info"><span class="comment-age">(31 Aug '13, 18:05)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-4681" class="comment-tools"></div><div class="clear"></div><div id="comment-4681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17238"></span>

<div id="answer-container-17238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17238-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is right meeting your requirement. <a href="https://github.com/caesar0301/pkt2flow">https://github.com/caesar0301/pkt2flow</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Dec '12, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/81988a1f30e4bd1169a9352b6991ae9d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jamin&#39;s gravatar image" /><p>Jamin<br />
<span class="score" title="17 reputation points">17</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jamin has no accepted answers">0%</span></p></div></div><div id="comments-container-17238" class="comments-container"></div><div id="comment-tools-17238" class="comment-tools"></div><div class="clear"></div><div id="comment-17238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

