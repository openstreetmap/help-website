+++
type = "question"
title = "What is the Content-type of wireshark .cap file?"
description = '''I use .cgi to capture files, and I want to download the file from the server side. I do not know the content-type of the .cap file, or is anyone know how to do? The file in server side can open successfully, but the downloaded file can not be opened. My .cgi code is: #!/bin/sh #=====================...'''
date = "2012-12-10T19:55:00Z"
lastmod = "2012-12-11T00:01:00Z"
weight = 16758
keywords = [ "content-type", "wireshark" ]
aliases = [ "/questions/16758" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What is the Content-type of wireshark .cap file?](/questions/16758/what-is-the-content-type-of-wireshark-cap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16758-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use .cgi to capture files, and I want to download the file from the server side. I do not know the content-type of the .cap file, or is anyone know how to do? The file in server side can open successfully, but the downloaded file can not be opened. My .cgi code is:</p><pre><code>#!/bin/sh
#=================================================
#   Main
# ================================================
fileis2=`ls /mnt/nfs/capture/`
file_size=`ls -l /mnt/nfs/capture/$fileis2 | awk &#39;{print $5}&#39;`
#echo $file_size
echo -e &quot;Content-Type:application/octet-stream&quot;
echo -e &quot;Accept-Ranges:bytes&quot;
echo -e &quot;Content-Length:$file_size&quot;
echo -e &quot;Content-Disposition:attachment;filename=$fileis2\n&quot;
cat $fileis2</code></pre><p>And what I think that cause the problem is the Content-Type. Mostly I found the appropriate type is binary file or the type octet-stream, but the result of the downloaded file can not be opened.</p><p>Any help appreciate!</p><p><img src="http://img542.imageshack.us/img542/5448/69830878.jpg" alt="File in server can be opened successfully" /> Downloaded file can not opened</p><p><img src="http://img341.imageshack.us/img341/1458/18953881.jpg" alt="Downloaded file can not opened" /></p><p>File in server can be opened successfully</p></div><div id="question-tags" class="tags-container tags">content-type wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '12, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/2131d0d11f07b1c9bc701ddce14e3715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shuinvy&#39;s gravatar image" /><p>Shuinvy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shuinvy has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 11 Dec '12, 01:35</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></img></div></div><div id="comments-container-16758" class="comments-container"></div><div id="comment-tools-16758" class="comment-tools"></div><div class="clear"></div><div id="comment-16758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16760"></span>

<div id="answer-container-16760" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16760-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The dialog box Wireshark popped up indicates that the file was successfully "opened", in the sense of lower-level file system "file open" calls, by Wireshark, and that Wireshark succeeded in reading the beginning of the file, <em>but</em> it did not recognize the data that it expected to be at the beginning of the file.</p><p>Capture files written by Wireshark (or TShark or dumpcap) are either pcap files or pcap-ng files. Capture files written by tcpdump are pcap files (although the tcpdump that comes with OS X Mountain Lion can also write pcap-ng files). Wireshark can also read a number of other types of capture files from other programs; however, the ".cap" file in question doesn't look, to Wireshark, like any type of file it can read.</p><p>Wireshark doesn't know the Content-Type for the file, and doesn't care what it is; it determines the file type based purely on the <em>contents</em> of the file. The only difference that the Content-Type would make would be to the client that's downloading the file; a Content-Type of application/octet-stream should work, even when transferring from a UN*X machine (as I infer your server is, unless you're using a lot of Cygwin in your CGI script) to a Windows machine (as I'm guessing the client is, from the Windows XP-style window decorations). If the client is running some form of UN*X, such as Linux or OS X or *BSD or Solaris or..., then the file will probably transfer without a problem with <em>any</em> Content-Type.</p><p>The problem probably isn't that Windows (or whatever the OS and desktop environment on the client is) isn't recognizing the content type, as Wireshark is trying to open the file; the problem is probably either that:</p><ul><li>the file wasn't a valid capture file of any type that Wireshark could read;</li><li>the file somehow got damaged when getting downloaded over HTTP;</li><li>there was an error and the file didn't get downloaded at all, and an error page or something such a that got "downloaded" to the file.</li></ul><p>I would suggest starting by debugging this with, err, umm, Wireshark - run Wireshark while the file is being downloaded and see what's getting transferred. If the file is a pcap file, the first 4 bytes of the <em>data</em> should either be A1 B2 C3 D4 or D4 C3 B2 A1; if it's a pcap-ng file, the first 4 bytes should be 0A 0D 0D 0A, the next 4 bytes after wouldn't have any particular guaranteed values, and the next 4 bytes after that should be 1A 2B 3C 4D or 4D 3C 2B 1A.</p><p>If you're still curious about the right Content-Type value for Wireshark capture files:</p><p>pcap files have a media type of <a href="http://www.iana.org/assignments/media-types/application/vnd.tcpdump.pcap">application/vnd.tcpdump.pcap</a>. The convention for those files is to give them an extension of .pcap, although other extensions, such as .dmp, .trc, .cap, etc. are used. I would not recommend using those other ones, as <em>all</em> of them have other meanings (".dmp" is used for some type of dump file, ".trc" was used by the old Sniffer software for DOS for Token Ring Captures, and ".cap" is used by at least two packet sniffers for their own capture file formats, plural).</p><p>pcap-ng files currently have no assigned media type. The convention for those files is to give them an extension of .pcapng.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '12, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16760" class="comments-container"><span id="16762"></span><div id="comment-16762" class="comment"><div id="post-16762-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot! Sorry about that I known the reason why my code is wrong. But I learned more! I will be care about it next time.</p></div><div id="comment-16762-info" class="comment-info"><span class="comment-age">(11 Dec '12, 00:17)</span> Shuinvy</div></div></div><div id="comment-tools-16760" class="comment-tools"></div><div class="clear"></div><div id="comment-16760-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16759"></span>

<div id="answer-container-16759" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16759-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry, I try it successfully by myself! And I post the solution if anyone require.</p><pre><code>echo -e &quot;Content-Type:application/cap&quot;</code></pre><p>The Content-type is just /cap, and the last line should be:</p><pre><code>cat /mnt/nfs/capture/&quot;$fileis2&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 21:25</strong></p><img src="https://secure.gravatar.com/avatar/2131d0d11f07b1c9bc701ddce14e3715?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shuinvy&#39;s gravatar image" /><p>Shuinvy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shuinvy has no accepted answers">0%</span></p></div></div><div id="comments-container-16759" class="comments-container"><span id="16761"></span><div id="comment-16761" class="comment"><div id="post-16761-score" class="comment-score"></div><div class="comment-text"><p>That's not the <em>correct</em> Content-Type for Wireshark capture files; see my answer. This suggests that the Capture-Type had nothing to do with the problem; the problem was with the last line of your script - the <code>cat</code> command in your original question wasn't passed the full pathname of the file, so it probably failed to open the file and returned an error, while the <code>cat</code> command in your answer <em>is</em> passed the full pathname of the file, so it successfully opened it. I'll bet "Content-Type: application/octet-stream" will work, as long as you use the new <code>cat</code> command.</p></div><div id="comment-16761-info" class="comment-info"><span class="comment-age">(11 Dec '12, 00:05)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16759" class="comment-tools"></div><div class="clear"></div><div id="comment-16759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

