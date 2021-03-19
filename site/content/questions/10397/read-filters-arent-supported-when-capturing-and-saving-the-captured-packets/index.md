+++
type = "question"
title = "Read filters aren&#x27;t supported when capturing and saving the captured packets."
description = '''Latest stable version 1.6.7 of TShark gives the following error message when trying to capture and save packets at the same time with read filter specified: C:&amp;gt;&quot;c:Program FilesWireshark_1.6.7tshark.exe&quot; -R sip -w file tshark: Read filters aren&#x27;t supported when capturing and saving the captured pa...'''
date = "2012-04-23T03:22:00Z"
lastmod = "2012-04-23T06:39:00Z"
weight = 10397
keywords = [ "read-filter", "saving", "capturing" ]
aliases = [ "/questions/10397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Read filters aren't supported when capturing and saving the captured packets.](/questions/10397/read-filters-arent-supported-when-capturing-and-saving-the-captured-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Latest stable version 1.6.7 of TShark gives the following error message when trying to capture and save packets at the same time with read filter specified:</p><p><strong>C:&gt;"c:Program FilesWireshark_1.6.7tshark.exe" -R sip -w file</strong></p><p>tshark: Read filters aren't supported when capturing and saving the captured packets.</p><p>This limitation was introduced in version 1.4.0. Earlier versions supported this combination:</p><p><strong>C:&gt;"c:Program FilesWireshark_1.3.5tshark.exe" -R sip -w file</strong></p><p>Capturing on Intel(R) 82566DM-2 Gigabit Network Connection (Microsoft's Packet Scheduler)</p><p>Comment in tshark.c is not too informative regarding this:</p><pre><code>    /* Currently, we don&#39;t support read filters when capturing
       and saving the packets. */
    if (rfilter != NULL) {
      cmdarg_err(&quot;Read filters aren&#39;t supported when capturing and saving the captured packets.&quot;);
      return 1;
    }</code></pre><p>Anyone knows why this limitation was introduced? Would it be possible to allow -R and -w at the same time again in latest version?</p><p>Laszlo BORTEL</p></div><div id="question-tags" class="tags-container tags">read-filter saving capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/5d07ce96d5b3b163b0cba6b773ba6145?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bortel&#39;s gravatar image" /><p>bortel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bortel has no accepted answers">0%</span></p></div></div><div id="comments-container-10397" class="comments-container"></div><div id="comment-tools-10397" class="comment-tools"></div><div class="clear"></div><div id="comment-10397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10399"></span>

<div id="answer-container-10399" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10399-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234">"bug" 2234</a>, this is expected behavior after the privilege separation that was created by introducing dumpcap as the capture engine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10399" class="comments-container"><span id="10432"></span><div id="comment-10432" class="comment"><div id="post-10432-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for the answer - though it does not make me happy.</p><p>Is there any workaround to simulate the old behaviour of TShark? Along the lines that I have read in bug 2234 I think of piping the output of the capturing TShark instance into the filtering TShark instance, like this:</p><p><strong>C:Program FilesWireshark_1.7.1&gt;tshark.exe -w- | tshark -i- -R dns</strong></p><p>Capturing on Standard input Capturing on Intel(R) 82566DM-2 Gigabit Network Connection (Microsoft's Packet Scheduler) tshark: Error reading from pipe: The operation completed successfully. (error 0)</p><p>0 packets captured 74</p><p>tshark: The file to which the capture was being saved ("-") could not be closed: Invalid argument.</p><p>But it does not seem to work on Windows XP with TShark version 1.7.1 ...</p></div><div id="comment-10432-info" class="comment-info"><span class="comment-age">(25 Apr '12, 03:30)</span> bortel</div></div></div><div id="comment-tools-10399" class="comment-tools"></div><div class="clear"></div><div id="comment-10399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

