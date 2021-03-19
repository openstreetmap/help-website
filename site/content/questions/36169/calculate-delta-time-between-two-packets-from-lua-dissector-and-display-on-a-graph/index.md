+++
type = "question"
title = "Calculate delta time between two packets from Lua dissector and display on a graph"
description = '''I&#x27;ve developed a Lua dissector for a custom protocol on top of the UDP protocol. Each initial packet sent will contain a reference number followed by a response message containing the same reference number, I would like to calculate the delta time between the two matching reference number packets an...'''
date = "2014-09-10T07:12:00Z"
lastmod = "2014-09-10T07:48:00Z"
weight = 36169
keywords = [ "lua", "dissector", "analysis", "packet", "graph" ]
aliases = [ "/questions/36169" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Calculate delta time between two packets from Lua dissector and display on a graph](/questions/36169/calculate-delta-time-between-two-packets-from-lua-dissector-and-display-on-a-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36169-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've developed a Lua dissector for a custom protocol on top of the UDP protocol. Each initial packet sent will contain a reference number followed by a response message containing the same reference number, I would like to calculate the delta time between the two matching reference number packets and display on a graph.</p><p>Currently I'm exporting the data to excel to calculate the delta and displaying on a graph, this is time consuming and I want to to make it more automated, but as a newbie to Wireshark development I'm not quite sure if it has the capabilities or the best way to achieve this task.</p><p>Any advice would be much appreciated.</p></div><div id="question-tags" class="tags-container tags">lua dissector analysis packet graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/8de5734b4f8fa841bfcf5498c22a9055?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chriswaddell87&#39;s gravatar image" /><p>chriswaddell87<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chriswaddell87 has no accepted answers">0%</span></p></div></div><div id="comments-container-36169" class="comments-container"></div><div id="comment-tools-36169" class="comment-tools"></div><div class="clear"></div><div id="comment-36169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36173"></span>

<div id="answer-container-36173" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36173-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Calculating the time delta in a Wireshark Lua script is not hard, but there is no way to have the results be graphed by Wireshark, other than to export the data to a file like you are now. Supporting such a thing has been on my to-do list (for the Qt version of Wireshark, not GTK, fwiw).</p><p>To calculate the delta time, you'd use a Lua table. The table's keys would be your protocol's reference numbers, and the values would be the time (use Lua's built-in <code>os.time()</code> or <code>os.clock()</code>). So when you get a request packet, you insert a new entry in the table of the ref number as the key and the current time as the value, and when you get a response you look up the ref number in the table, and subtract the entry's time value from current time. (actually you'll want to do the lookup first on the request too, in case the request is retransmitted, since you want to use the originally transmitted request time presumably)</p><p>Also remember to clear the table before each run of the capture, so that it won't grow forever as people open/close capture files or start/restart live capturing of your protocol. The easiest way to do this is to clear the table (i.e., reset the variable to a new table) in the <code>myproto.init()</code> function for your new protocol. The <code>init()</code> function is automatically called by Wireshark, similar to the <code>dissector()</code> one, but it's called each time a new capture file is opened or a live capture is started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-36173" class="comments-container"><span id="36206"></span><div id="comment-36206" class="comment"><div id="post-36206-score" class="comment-score"></div><div class="comment-text"><p>I would have to check the refNumber against two other variables to rule out if it was a repeat message and then use each frame.time_relative value. I can't use the refNubmer as a key, due to some message types containing the same refNumber which would overwrite the original key. At what stage should the Lua table be implemented, at the dissector or listener ?</p></div><div id="comment-36206-info" class="comment-info"><span class="comment-age">(11 Sep '14, 10:47)</span> chriswaddell87</div></div><span id="36269"></span><div id="comment-36269" class="comment"><div id="post-36269-score" class="comment-score"></div><div class="comment-text"><p>That's up to you really - I mean the Lua variable holding the table needs to be defined outside of both the dissector and listener functions, since it needs to live for the duration; but you can add/lookup in it in the dissector or listener. (note: be aware that a dissector will be called multiple times for the same packet)</p></div><div id="comment-36269-info" class="comment-info"><span class="comment-age">(12 Sep '14, 07:37)</span> Hadriel</div></div><span id="36308"></span><div id="comment-36308" class="comment"><div id="post-36308-score" class="comment-score">1</div><div class="comment-text"><p>I have a LUA script where I just want to run some code on Wireshark's first scan of the packets. I use the statement:</p><p>if not pinfo.visited then</p><p>As you'd expect, pinfo.visited is not set on the first scan.</p></div><div id="comment-36308-info" class="comment-info"><span class="comment-age">(14 Sep '14, 02:06)</span> PaulOfford</div></div></div><div id="comment-tools-36173" class="comment-tools"></div><div class="clear"></div><div id="comment-36173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

