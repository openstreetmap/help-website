+++
type = "question"
title = "tshark rotating pcap files"
description = '''Would it be possible to have tshark generate rotating pcap files just like this? I could not find much documentation about it. '''
date = "2015-07-24T14:51:00Z"
lastmod = "2015-08-03T08:47:00Z"
weight = 44454
keywords = [ "pcap", "tcpdump", "tshark" ]
aliases = [ "/questions/44454" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [tshark rotating pcap files](/questions/44454/tshark-rotating-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44454-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Would it be possible to have tshark generate rotating pcap files just like <a href="https://clutterbox.de/2010/08/tcpdump-with-rotating-capture-files/">this</a>?</p><p>I could not find much documentation about it.</p></div><div id="question-tags" class="tags-container tags">pcap tcpdump tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/f8e9cc3c86f1d1814aa3a51408d9e4b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob328080&#39;s gravatar image" /><p>Bob328080<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob328080 has no accepted answers">0%</span></p></div></div><div id="comments-container-44454" class="comments-container"></div><div id="comment-tools-44454" class="comment-tools"></div><div class="clear"></div><div id="comment-44454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="44456"></span>

<div id="answer-container-44456" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44456-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Look at the tshark options for capture stop &amp; output, similar to tcpdump, but not quite the same:</p><pre><code>Capture stop conditions:                                                     
  -c &lt;packet count&gt;        stop after n packets (def: infinite)              
  -a &lt;autostop cond.&gt; ...  duration:NUM - stop after NUM seconds             
                           filesize:NUM - stop this file after NUM KB        
                              files:NUM - stop after NUM files               
Capture output:                                                              
  -b &lt;ringbuffer opt.&gt; ... duration:NUM - switch to next file after NUM secs 
                           filesize:NUM - switch to next file after NUM KB   
                              files:NUM - ringbuffer: replace after NUM files</code></pre><p>You're probably looking for the <code>-b</code> ringbuffer option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44456" class="comments-container"></div><div id="comment-tools-44456" class="comment-tools"></div><div class="clear"></div><div id="comment-44456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44457"></span>

<div id="answer-container-44457" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44457-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am not sure I understand the question properly, but if I did:</p><p>Please always remember to use -? or --help, according to "tshark -?" output:</p><pre><code>Capture output:
-b &lt;ringbuffer opt.&gt; ... duration:NUM - switch to next file after NUM secs
                         filesize:NUM - switch to next file after NUM KB
                         files:NUM - ringbuffer: replace after NUM files</code></pre><p>-b duration:600 files 7 will give you a 70 minute ring buffer (rotation). If this is not what you meant, please clarify your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p>DarrenWright<br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44457" class="comments-container"></div><div id="comment-tools-44457" class="comment-tools"></div><div class="clear"></div><div id="comment-44457-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="44789"></span>

<div id="answer-container-44789" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44789-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tshark -a filesize:10000 -b files:20 -i &lt; INTERFACE &gt; -w &lt; BASE_FILE_NAME.pcapng &gt;</code></p><p>will give you a rotating set of 20 files each of which will be (if my math is correct) 10 mb in size. The same thing can be accomplished using -b in place of the -a. [Up to this point I have found no difference between the two.]</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/0a92214fd94d818059f740cdd56be7af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greenfreq&#39;s gravatar image" /><p>greenfreq<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greenfreq has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Aug '15, 08:48</p></div></div><div id="comments-container-44789" class="comments-container"></div><div id="comment-tools-44789" class="comment-tools"></div><div class="clear"></div><div id="comment-44789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

