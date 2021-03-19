+++
type = "question"
title = "Filtering NX responses from a pcap file"
description = '''I am using the following command:  tshark -r whatever -T fields -e dns.qry.name -e dns.flags.rcode -Y &quot;dns.qry.name contains drush and dns.flags.response eq 1 and dns.flags.rcode != 0&quot;  for retrieving the SERVFAILures and the NX responses but it complains with:   tshark: Lua: Error during loading:  ...'''
date = "2016-03-02T02:53:00Z"
lastmod = "2016-03-02T03:30:00Z"
weight = 50646
keywords = [ "filter", "dns" ]
aliases = [ "/questions/50646" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering NX responses from a pcap file](/questions/50646/filtering-nx-responses-from-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50646-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the following command:</p><pre><code> tshark -r whatever -T fields -e dns.qry.name -e dns.flags.rcode -Y &quot;dns.qry.name contains drush and dns.flags.response eq 1 and dns.flags.rcode != 0&quot;</code></pre><p>for retrieving the SERVFAILures and the NX responses but it complains with:</p><pre><code> tshark: Lua: Error during loading:
 [string &quot;/usr/share/wireshark/init.lua&quot;]:46: dofile has been disabled due to running Wireshark as superuser. See http://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user.</code></pre><p>I also tried running this command from a non-privileged account (not root) against a pcap file that had NX responses but nothing was returned...</p><p>Is there another way of doing it or a fix for this?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">filter dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '16, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/93eb17372bd105d80fc159bb1c97d6fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="altdrugzgene&#39;s gravatar image" /><p>altdrugzgene<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="altdrugzgene has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Mar '16, 04:37</p></div></div><div id="comments-container-50646" class="comments-container"><span id="50665"></span><div id="comment-50665" class="comment"><div id="post-50665-score" class="comment-score"></div><div class="comment-text"><ul><li><p>"another way of doing it" is to run tshark as a non-root; as you are reading the input from a file rather than capturing it, you definitely do not need the root privileges.</p></li><li><p>"a fix for this" will never come as fixes come for bugs, not for intentional safety measures. Wireshark/tshark intentionally disable Lua when running with root privileges, and they also intentionally spawn dumpcap as a separate process to run with root privileges and do only the capturing, so that they themselves could run <em>without</em> root privileges.</p></li></ul></div><div id="comment-50665-info" class="comment-info"><span class="comment-age">(02 Mar '16, 04:42)</span> sindy</div></div><span id="50682"></span><div id="comment-50682" class="comment"><div id="post-50682-score" class="comment-score"></div><div class="comment-text"><p>the thing is that i want a filter to see the NX responses and other SERVFAIL messages of DNS. I tried running this with a standard account and filter didnt work.</p></div><div id="comment-50682-info" class="comment-info"><span class="comment-age">(02 Mar '16, 08:15)</span> altdrugzgene</div></div><span id="50683"></span><div id="comment-50683" class="comment"><div id="post-50683-score" class="comment-score"></div><div class="comment-text"><p>Once again in a different thread.</p><p>If, on the same capture on which it does not work for you:</p><ul><li><p>it works elsewhere, it is most likely some issue with your configuration or, less likely, installation.</p></li><li><p>it does not work elsewhere, it is most likely something about the packet which the dissector cannot handle.</p></li></ul><p>To find out which investigation way to take, we need your capture. Without it, we cannot help you.</p></div><div id="comment-50683-info" class="comment-info"><span class="comment-age">(02 Mar '16, 08:27)</span> sindy</div></div></div><div id="comment-tools-50646" class="comment-tools"></div><div class="clear"></div><div id="comment-50646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50651"></span>

<div id="answer-container-50651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50651-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you followed the link in the "complaint"? It's telling you to really, really abstain from running tshark as root. The link show how to configure your system so that you can capture without running tshark (or wireshark) as root.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '16, 03:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-50651" class="comments-container"><span id="50653"></span><div id="comment-50653" class="comment"><div id="post-50653-score" class="comment-score"></div><div class="comment-text"><p>my question is not clear I think. Is the lua scripting language NOT working if u execute wireshark as root?</p></div><div id="comment-50653-info" class="comment-info"><span class="comment-age">(02 Mar '16, 03:37)</span> altdrugzgene</div></div><span id="50656"></span><div id="comment-50656" class="comment"><div id="post-50656-score" class="comment-score"></div><div class="comment-text"><p>Yes it is disabled.</p></div><div id="comment-50656-info" class="comment-info"><span class="comment-age">(02 Mar '16, 03:50)</span> grahamb ♦</div></div><span id="50666"></span><div id="comment-50666" class="comment"><div id="post-50666-score" class="comment-score"></div><div class="comment-text"><p>However it doesnt work even when im running it from an unprivileged account</p></div><div id="comment-50666-info" class="comment-info"><span class="comment-age">(02 Mar '16, 04:47)</span> altdrugzgene</div></div><span id="50667"></span><div id="comment-50667" class="comment"><div id="post-50667-score" class="comment-score"></div><div class="comment-text"><p>OK, so that was really unclear that Lua is not your primary problem.</p><p>Can you provide a capture where it fails for you? I've just randomly taken a capture and used your filter with modified search string and it worked for me the following way (a little bit of manual obfuscation on the real fqdn done):</p><pre><code>C:\Users\me&gt;&quot;c:\Program Files\Wireshark\tshark.exe&quot; -r &quot;c:\Users\me\Downloads\random.pcapng&quot; -Y &quot;dns.qry.name contains searchstring and dns.flags.response eq 1 and dns.flags.rcode != 0&quot; -T fields -e dns.qry.name -e dns.flags.rcode

my.searchstring.org    3</code></pre></div><div id="comment-50667-info" class="comment-info"><span class="comment-age">(02 Mar '16, 05:00)</span> sindy</div></div><span id="50679"></span><div id="comment-50679" class="comment"><div id="post-50679-score" class="comment-score"></div><div class="comment-text"><p>well it doesnt work for me... i want a filter that spits all the NX and SERVFAIL responses but my filter doesnt work</p></div><div id="comment-50679-info" class="comment-info"><span class="comment-age">(02 Mar '16, 07:59)</span> altdrugzgene</div></div><span id="50680"></span><div id="comment-50680" class="comment not_top_scorer"><div id="post-50680-score" class="comment-score"></div><div class="comment-text"><p>Can you post a capture file with examples of such two packets (NX and SERVFAIL, one per each type is enough, so you may use <code>File-&gt;Export Specified Packets</code> if you don't want to disclose too much information) somewhere and edit your original question with a link to it? That should answer whether it is a generic issue (means: a bug worth reporting) or something about your installation.</p></div><div id="comment-50680-info" class="comment-info"><span class="comment-age">(02 Mar '16, 08:07)</span> sindy</div></div><span id="50681"></span><div id="comment-50681" class="comment not_top_scorer"><div id="post-50681-score" class="comment-score"></div><div class="comment-text"><p>That (modified as appropriate) filter works for me as well. What version of Wireshark are you using?</p><p>@altdrugzgene, is it possible to post a link to your capture, or at least a capture with one pdu from it that is the failure you want to locate?</p></div><div id="comment-50681-info" class="comment-info"><span class="comment-age">(02 Mar '16, 08:12)</span> grahamb ♦</div></div></div><div id="comment-tools-50651" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-50651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

