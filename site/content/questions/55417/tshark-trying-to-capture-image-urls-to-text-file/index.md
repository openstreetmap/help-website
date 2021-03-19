+++
type = "question"
title = "TSHARK trying to capture image URLs to text file"
description = '''I am trying to capture to text file the url&#x27;s of images downloaded during an interval of a minute via wi-fi on Windows 10 home. I have installed Wireshark 2.0.5 and it works. However, although I can capture traffic to file, for the life of me I cannot get a suitable display or capture filter to work...'''
date = "2016-09-09T01:52:00Z"
lastmod = "2016-09-12T06:49:00Z"
weight = 55417
keywords = [ "url", "capture", "image", "tshark" ]
aliases = [ "/questions/55417" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TSHARK trying to capture image URLs to text file](/questions/55417/tshark-trying-to-capture-image-urls-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55417-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to capture to text file the url's of images downloaded during an interval of a minute via wi-fi on Windows 10 home. I have installed Wireshark 2.0.5 and it works. However, although I can capture traffic to file, for the life of me I cannot get a suitable display or capture filter to work. Can someone please tell me where I am going wrong?</p><p>Here are my failures:</p><pre><code>C:\Program Files\Wireshark&gt;tshark -a duration:60 -w c:\temp\shout.txt http.content_type ==&quot;image&quot; 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.contenttype ==image&quot; for interface &#39;Wi-Fi&#39;.

That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).

Note that display filters and capture filters don&#39;t have the same syntax, so you can&#39;t use most display filter expressions as capture filters.

See the User&#39;s Guide for a description of the capture filter syntax.

C:\Program Files\Wireshark&gt;tshark -a duration:60 http.content_type ==&quot;image&quot; 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.content_type ==image&quot; for interface &#39;Wi-Fi&#39;.

That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).

Note that display filters and capture filters don&#39;t have the same syntax, so you can&#39;t use most display filter expressions as capture filters.

See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark -a duration:60 -w c:\temp\shout.txt -f http.content_type ==&quot;image&quot; 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark -a duration:60 -f http.content_type ==&quot;image&quot; 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark -a duration:60 http.content_type ==&quot;image&quot; 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.content_type ==image&quot; for interface &#39;Wi-Fi&#39;.

That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).

Note that display filters and capture filters don&#39;t have the same syntax, so you can&#39;t use most display filter expressions as capture filters.

See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark -f http.content_type ==&quot;image&quot; 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark -f &#39;http.content_type ==&quot;image&quot;&#39; 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark -f &#39;http.content_type ==image 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark http.content_type ==image 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.content_type ==image&quot; for interface &#39;Wi-Fi&#39;.

That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).

Note that display filters and capture filters don&#39;t have the same syntax, so you can&#39;t use most display filter expressions as capture filters.

See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark http.content_type == image 
Capturing on &#39;Wi-Fi&#39; tshark: Invalid capture filter &quot;http.content_type == image&quot; for interface &#39;Wi-Fi&#39;.

That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).

Note that display filters and capture filters don&#39;t have the same syntax, so you can&#39;t use most display filter expressions as capture filters.

See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark http.content_type == image -w c:\temp\shout.txt 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.content_type == image -w c:\temp\shout.txt&quot; for interface &#39;Wi-Fi&#39;.

That string isn&#39;t a valid capture filter (syntax error). See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark http.content_type == &quot;image&quot; -w c:\temp\shout.txt 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;http.content_type == image -w c:\temp\shout.txt&quot; for interface &#39;Wi-Fi&#39;.

That string isn&#39;t a valid capture filter (syntax error). See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark &#39;http.content_type == &quot;image&quot;&#39; -w c:\temp\shout.txt 
Capturing on &#39;Wi-Fi&#39; 
tshark: Invalid capture filter &quot;&#39;http.content_type == image&#39; -w c:\temp\shout.txt&quot; for interface &#39;Wi-Fi&#39;.

That string isn&#39;t a valid capture filter (illegal token). See the User&#39;s Guide for a description of the capture filter syntax. 0 packets captured

C:\Program Files\Wireshark&gt;tshark -f &#39;http.content_type == &quot;image&quot;&#39; -w c:\temp\shout.txt 
tshark: A default capture filter was specified both with &quot;-f&quot; and with additional command-line arguments.

C:\Program Files\Wireshark&gt;tshark -v TShark (Wireshark) 2.0.5 (v2.0.5-0-ga3be9c6 from master-2.0)

Copyright 1998-2016 Gerald Combs and contributors. License GPLv2+: GNU GPL version 2 or later This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (32-bit) with WinPcap (413), with libz 1.2.8, with GLib 2.38.0, with SMI 0.4.8, with c-ares 1.11.0, with Lua 5.2, with GnuTLS 3.2.15, with Gcrypt 1.6.2, with MIT Kerberos, with GeoIP.

Running on 32-bit Windows 10, build 10586, with locale EnglishUnited Kingdom.1252, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 10_rel0b (20091008), with GnuTLS 3.2.15, with Gcrypt 1.6.2. Intel(R) Atom(TM) CPU N550 @ 1.50GHz, with 2038MB of physical memory.

Built using Microsoft Visual C++ 12.0 build 40629

C:\</code></pre></div><div id="question-tags" class="tags-container tags">url capture image tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '16, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/8c4a259dca35232d167ee93f9e6d0afd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeWa&#39;s gravatar image" /><p>MikeWa<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeWa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '16, 02:18</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-55417" class="comments-container"></div><div id="comment-tools-55417" class="comment-tools"></div><div class="clear"></div><div id="comment-55417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="55419"></span>

<div id="answer-container-55419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55419-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The responses of the form:</p><pre><code>That string looks like a valid display filter; however, it isn&#39;t a valid capture filter (syntax error).</code></pre><p>give the answer. <code>http.content_type=="image"</code> is a display filter so you should use it with the <code>-Y</code> flag, e.g. <code>tshark -a duration:60 -Y http.content_type=="image"</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '16, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '16, 06:12</p></div></div><div id="comments-container-55419" class="comments-container"><span id="55421"></span><div id="comment-55421" class="comment"><div id="post-55421-score" class="comment-score"></div><div class="comment-text"><p>Wow - fast response, thanks - BUT I still get the error:</p><p>C:\Program Files\Wireshark&gt;tshark -a duration:60 -Y http.content_type =="image" -w c:\temp\shout.txt Capturing on 'Wi-Fi' tshark: Invalid capture filter "==image -w c:\temp\shout.txt" for interface 'Wi-Fi'.</p><p>That string isn't a valid capture filter (syntax error). See the User's Guide for a description of the capture filter syntax. 0 packets captured</p></div><div id="comment-55421-info" class="comment-info"><span class="comment-age">(09 Sep '16, 02:34)</span> MikeWa</div></div><span id="55423"></span><div id="comment-55423" class="comment"><div id="post-55423-score" class="comment-score"></div><div class="comment-text"><p>The <code>==</code> in the display filter syntax confuses the shell, but although that can be fixed by closing the whole display filter expression into a pair of quotes as below rather than just the "image" part of it,</p><p><code>tshark.exe -a duration:60 -Y "http.content_type == image" -w c:\temp\shout.txt</code></p><p>you'll get another error:</p><p><code>tshark: Display filters aren't supported when capturing and saving the captured packets.</code></p><p>So bad luck here, you'll have to capture with just a capture filter (if you can define one narrow enough to make sense for your case), and use display filter later to further limit the result.</p></div><div id="comment-55423-info" class="comment-info"><span class="comment-age">(09 Sep '16, 02:53)</span> sindy</div></div><span id="55431"></span><div id="comment-55431" class="comment"><div id="post-55431-score" class="comment-score"></div><div class="comment-text"><blockquote>The == in the display filter syntax confuses the shell</blockquote><p>Sorry, I had used one of the earlier attempts without spaces around the <code>==</code> and that does work on both PowerShell and Cmd shells. I've fixed my answer.</p><p>That doesn't help with the desire to capture and write to a file with a display filter though.</p></div><div id="comment-55431-info" class="comment-info"><span class="comment-age">(09 Sep '16, 06:11)</span> grahamb ♦</div></div><span id="55445"></span><div id="comment-55445" class="comment"><div id="post-55445-score" class="comment-score"></div><div class="comment-text"><p>After a while writing powershell regular expressions to filter the "raw" capture without the image filter I read your second reply.</p><p>The command</p><p>tshark -a duration:60 -Y "http.content_type == image"</p><p>does indeed run, but it does not capture any image packet URLs.</p><p>I smell rats in the documentation, or worse, the software.</p><p>Mike</p></div><div id="comment-55445-info" class="comment-info"><span class="comment-age">(09 Sep '16, 14:01)</span> MikeWa</div></div><span id="55446"></span><div id="comment-55446" class="comment"><div id="post-55446-score" class="comment-score"></div><div class="comment-text"><p>Of course, while I am sampling, I am running web queries to generate the traffic I need to catch, and this works well using:</p><p>tshark - duration:60 -w c:\temp\shout.txt tcp port 80</p><p>followed by :</p><p>tshark -r c:\temp\shout.txt -z http_req,tree &gt;c:\temp\shouta.txt</p><p>and further treatment with regular expressions in Powershell</p><p>but is a far cry from what the Wireshark documentation led me to believe was possible.</p></div><div id="comment-55446-info" class="comment-info"><span class="comment-age">(09 Sep '16, 14:19)</span> MikeWa</div></div><span id="55448"></span><div id="comment-55448" class="comment not_top_scorer"><div id="post-55448-score" class="comment-score"></div><div class="comment-text"><p>Can you publish a sample capture file together with an example of what would be your desired tshark output so that I could check (using the latest available tshark, 2.2.0) whether there is no misunderstanding between what you want and what tshark can do? It is not possible to upload a capture file to this site directly, you have to use <a href="https://www.cloudshark.org/">Cloudshark</a> or any plain file sharing service and place a login-free link to the capture here.</p></div><div id="comment-55448-info" class="comment-info"><span class="comment-age">(09 Sep '16, 14:47)</span> sindy</div></div><span id="55485"></span><div id="comment-55485" class="comment not_top_scorer"><div id="post-55485-score" class="comment-score"></div><div class="comment-text"><p>Hello - Thanks Sindy for this helpful suggestion.</p><p>The capture file I have contains the complete set of records captured by the call " tshark -a duration:60 -w &lt;some path=""&gt; tcp port 80 "</p><p>What I am trying to do is pretty simple - I would like to use a Powershell script to launch tshark to capture all the URLs containing images (ideally by type jpg, gif) loaded by a browser on the local machine during a short defined period, and to save these URLs to a text file.</p><p>I am using the display filter "-z http_req,tree " and then filtering in Powershell.</p><p>In fact just saving the HTTP requests by HTTP host as text would almost get me there.</p><p>Mike</p></div><div id="comment-55485-info" class="comment-info"><span class="comment-age">(12 Sep '16, 06:15)</span> MikeWa</div></div></div><div id="comment-tools-55419" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-55419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55486"></span>

<div id="answer-container-55486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55486-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately the info you require is contained in two different packets, the "Content-Type:" header that indicates an image is in the response, and the URI is in the associated request. Wireshark filters, (display or capture) only operate on a single packet at a time to include or exclude that packet and do not allow the selection of 1 packet based on the content of another.</p><p>I can think of two ways to proceed:</p><ul><li>Do two runs over the capture, the first identifies the frame number of request packets and the second run builds a filter for those packets, in both cases use the <code>-T fields -e xxx</code> option to limit the output to the items required, e.g.</li></ul><pre><code>$frames = tshark -r file -T fields -e http.request.in http.content_type contains image
$filter = &quot;&quot;
foreach($frame in $frames) {
    if ($filter -eq &quot;&quot;) {
        $filter = &quot;frame.number == $frame&quot;
    }
    else {
        $filter += &quot; or frame.number == $frame&quot;
    }
}
tshark -r file -T fields -e http.request.full_uri $filter</code></pre><p>or</p><ul><li>Use <a href="https://wiki.wireshark.org/Mate">MATE</a> to build an association between the packets and add the URL to the response.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Sep '16, 06:54</p></div></div><div id="comments-container-55486" class="comments-container"><span id="55492"></span><div id="comment-55492" class="comment"><div id="post-55492-score" class="comment-score"></div><div class="comment-text"><p>Graham - Many thanks for the post (and the re-formatted version) - this has helped me well on my way and I am getting what I need - testing the Powershell now.</p><p>Thanks a lot,</p><p>Mike</p></div><div id="comment-55492-info" class="comment-info"><span class="comment-age">(12 Sep '16, 10:08)</span> MikeWa</div></div><span id="55493"></span><div id="comment-55493" class="comment"><div id="post-55493-score" class="comment-score"></div><div class="comment-text"><p>The only caveat with the first option is if there are a lot of image requests then the resulting <code>$filter</code> string may exceed the maximum command line limit.</p></div><div id="comment-55493-info" class="comment-info"><span class="comment-age">(12 Sep '16, 10:46)</span> grahamb ♦</div></div></div><div id="comment-tools-55486" class="comment-tools"></div><div class="clear"></div><div id="comment-55486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

