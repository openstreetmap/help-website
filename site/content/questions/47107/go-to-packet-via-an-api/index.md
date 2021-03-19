+++
type = "question"
title = "&quot;Go to packet&quot; via an API"
description = '''Hi, We are working on a proof of concept that includes a facility to remotely interact with Wireshark. We want to start with one simple function; sending a command to an instance of Wireshark to tell it to jump to a particular packet number. So basically we want to programatically call the &quot;Go to pa...'''
date = "2015-10-31T06:24:00Z"
lastmod = "2015-11-05T08:59:00Z"
weight = 47107
keywords = [ "plugin" ]
aliases = [ "/questions/47107" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# ["Go to packet" via an API](/questions/47107/go-to-packet-via-an-api)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47107-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are working on a proof of concept that includes a facility to remotely interact with Wireshark. We want to start with one simple function; sending a command to an instance of Wireshark to tell it to jump to a particular packet number. So basically we want to programatically call the "Go to packet" function.</p><p>We want this functionality to be implemented through a plugin rather than change any Wireshark code. So the idea is to write a post-dissector (in C) whose registration function spins up a TCP-based service on a new thread that listens on a port for an incoming external command (in this case a "Go to packet" command) and then actions the command.</p><p>For this proof of concept we just need this to work with Wireshark v2 (i.e. Qt) and Windows.</p><p>I'll get to the point. Is there an API for C plugins that we can use to call the Go to packet function?</p><p>Alternatively, I've looked through the code at the UI interface and notice there is a callback function goto_frame_cb which I guess is called when the button is pressed in the Go to dialogue, but I also notice this is for GTK. Is there a Qt equivalent? Would this be a way to achieve what we are trying to achieve?</p><p>Am I being stupid by not realising that this functionality already exists?</p><p>Any advice would be much appreciated.</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '15, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-47107" class="comments-container"><span id="47110"></span><div id="comment-47110" class="comment"><div id="post-47110-score" class="comment-score"></div><div class="comment-text"><p>Did you try calling wireshark.exe with the -g parameter? It jumps to the packet number that you specify on start.</p><p>But I guess you want to interactively jump to packets in already opened instances of Wireshark?</p></div><div id="comment-47110-info" class="comment-info"><span class="comment-age">(31 Oct '15, 10:12)</span> Jasper ♦♦</div></div><span id="47120"></span><div id="comment-47120" class="comment"><div id="post-47120-score" class="comment-score"></div><div class="comment-text"><p>Paul, what's the purpose of doing that within the running GUI application? If we understand your needs, we might come up with other ideas as well.</p></div><div id="comment-47120-info" class="comment-info"><span class="comment-age">(31 Oct '15, 15:39)</span> Kurt Knochner ♦</div></div><span id="47128"></span><div id="comment-47128" class="comment"><div id="post-47128-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, You're right - We need to move the current position within an already loaded Wireshark instance.</p><p>Hi Kurt, There's not much more to tell. We want an external application that we have written to be able to move the current packet position within a trace already loaded into Wireshark.</p><p>Thanks and regards...Paul</p></div><div id="comment-47128-info" class="comment-info"><span class="comment-age">(01 Nov '15, 01:34)</span> PaulOfford</div></div></div><div id="comment-tools-47107" class="comment-tools"></div><div class="clear"></div><div id="comment-47107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47299"></span>

<div id="answer-container-47299" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47299-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Paul,</p><p>did you have a look at the <a href="https://code.wireshark.org/review/#/c/9939/">PluginIF</a> work done by Roland Knall and that is part of the upcoming Wireshark 2.0? From what I understand it allows you to develop a plugin menu and the "Go to frame" case is part of the API.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '15, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-47299" class="comments-container"><span id="47310"></span><div id="comment-47310" class="comment"><div id="post-47310-score" class="comment-score"></div><div class="comment-text"><p>That is a great call Pascal. That looks to be exactly what I want. I followed your PluginIF link but I can't find any documentation, or even a brief description. I've looked at the code and I think I can see how I could use it but some doc would be good.</p></div><div id="comment-47310-info" class="comment-info"><span class="comment-age">(05 Nov '15, 10:21)</span> PaulOfford</div></div></div><div id="comment-tools-47299" class="comment-tools"></div><div class="clear"></div><div id="comment-47299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47150"></span>

<div id="answer-container-47150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47150-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Hi Kurt, There's not much more to tell. We want an external application that we have written to be able to move the current packet position within a trace already loaded into Wireshark.</p></blockquote><p>well, then maybe the easiest way would be to use a GUI automation tool like <a href="https://www.autoitscript.com/site/autoit/"><strong>AutoIT</strong></a> or <a href="http://www.autohotkey.com/"><strong>AutoHotKey</strong></a>. I've worked quite a lot with <strong>AutoIT</strong> to automate several things on Windows, however not yet anything for Wireshark.</p><p>Idea:</p><ol><li>Get the focus of the GUI window you're after (see tool docs)</li><li>Let the tool send 'CTRL-g' to the window</li><li>Let the tool send the line number and \&lt;ENTER&gt;</li></ol><p>Maybe you can find some examples in the forums of these tools.</p><blockquote><p><a href="https://www.autoitscript.com/forum/">https://www.autoitscript.com/forum/</a><br />
<a href="http://www.autohotkey.com/boards/">http://www.autohotkey.com/boards/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '15, 04:18</p></div></div><div id="comments-container-47150" class="comments-container"></div><div id="comment-tools-47150" class="comment-tools"></div><div class="clear"></div><div id="comment-47150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47114"></span>

<div id="answer-container-47114" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47114-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there an API for C plugins that we can use to call the Go to packet function?</p></blockquote><p>There will probably never be one for use in <em>dissectors</em>, as they might not be invoked from within a program with a GUI.</p><p>For use in <em>GUI</em> plugins, you can call <code>cf_goto_frame()</code>; the first argument is a <code>capture_file *cf</code>, and the second argument is a <code>guint</code> which is the frame number (starting with 1). Unfortunately, finding the appropriate <code>capture_file *cf</code> is a bit of work in the Qt code.</p><p>(That could be found by looking at <code>goto_frame_cb()</code>, noticing that it creates the dialog rather than actually going to the frame and that the "Ok" button calls <code>goto_frame_ok_cb()</code>, looking at <code>goto_frame_ok_cb()</code> and noticing that, after it validates the frame number typed into the dialog, it calls <code>cf_goto_frame()</code> and, if that succeeds, dismisses the "go to" dialog.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '15, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Nov '15, 05:57</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-47114" class="comments-container"><span id="47129"></span><div id="comment-47129" class="comment"><div id="post-47129-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy, I'll look into this.</p></div><div id="comment-47129-info" class="comment-info"><span class="comment-age">(01 Nov '15, 01:35)</span> PaulOfford</div></div><span id="47291"></span><div id="comment-47291" class="comment"><div id="post-47291-score" class="comment-score"></div><div class="comment-text"><p>I have used VS to trace what happens when you enter a frame number and click on go. The stack shows a load of QT stuff, then:</p><pre><code>Wireshark.exe!MainWindow::gotoFrame(int packet_num) Line 3463   C++
Wireshark.exe!MainWindow::on_goToGo_clicked() Line 3306 C++
Wireshark.exe!MainWindow::qt_static_metacall(QObject * _o,  QMetaObject::Call _c, int _id, void * * _a) Line 1515   C++
Wireshark.exe!MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void * * _a) Line 1708 C++
Qt5Cored.dll!000000006711a724() Unknown
.
.</code></pre><p>The code looks like this:</p><pre><code>void MainWindow::gotoFrame(int packet_num)
{
    if ( packet_num &gt; 0 )
    {
        packet_list_-&gt;goToPacket(packet_num);
    }
}</code></pre><p>packet_list_ is a type PacketList and instantiated in the MainWindow class. And the MainWindow it's using has a global pointer gbl_cur_main_window.</p><p>So my theory is that in the plugin dissector I need to get a copy of the packet_list_ pointer and call goToPacket:</p><pre><code>PacketList *my_packet_list_ = gbl_cur_main_window.packet_list;

my_packet_list_-&gt;goToPacket(55);</code></pre><p>Does that seem feasible?</p><p>Thanks and regards...Paul</p></div><div id="comment-47291-info" class="comment-info"><span class="comment-age">(05 Nov '15, 05:52)</span> PaulOfford</div></div></div><div id="comment-tools-47114" class="comment-tools"></div><div class="clear"></div><div id="comment-47114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

