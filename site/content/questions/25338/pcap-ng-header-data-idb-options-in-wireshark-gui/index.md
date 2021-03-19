+++
type = "question"
title = "PCAP-NG header data (IDB options) in Wireshark GUI"
description = '''My program writes PCAP-NG files. I open them with Wireshark. Among others, my program writes in the Section Header Block its name and a description of the platform (options shb_ hardware, shb_ os, shb_ userappl) and for each Interface Description Block a description of the network interface and the ...'''
date = "2013-09-29T02:36:00Z"
lastmod = "2016-12-14T10:16:00Z"
weight = 25338
keywords = [ "gui", "pcap-ng", "idb", "options" ]
aliases = [ "/questions/25338" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP-NG header data (IDB options) in Wireshark GUI](/questions/25338/pcap-ng-header-data-idb-options-in-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25338-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25338-score" class="post-score" title="current number of votes">0</div><span id="post-25338-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My program writes PCAP-NG files. I open them with Wireshark.</p><p>Among others, my program writes in the Section Header Block its name and a description of the platform (options shb_ hardware, shb_ os, shb_ userappl) and for each Interface Description Block a description of the network interface and the capture filter (options if_ description and if_ filter).</p><p>All these data i can see when i open the dump file with Wireshark and look at Statistics-&gt;Summary.</p><p>My program writes other data in the dump file: in each Interface Description Block, it also writes the system name of the network interface, as well as its IPv4 addresses and its MAC address (options if_ name, if_ IPv4addr and if_ MACaddr).</p><p>These latter data i can't see through Wireshark. Do i miss something in Wireshark's GUI or is there any utility that reads PCAP-NG files and puts out all these fields?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-pcap-ng" rel="tag" title="see questions tagged &#39;pcap-ng&#39;">pcap-ng</span> <span class="post-tag tag-link-idb" rel="tag" title="see questions tagged &#39;idb&#39;">idb</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '13, 02:36</strong></p><img src="https://secure.gravatar.com/avatar/0c4a0d3634bb05bf810ee1b5fe13ec54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ime-braun&#39;s gravatar image" /><p><span>ime-braun</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ime-braun has no accepted answers">0%</span></p></div></div><div id="comments-container-25338" class="comments-container"></div><div id="comment-tools-25338" class="comment-tools"></div><div class="clear"></div><div id="comment-25338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25339"></span>

<div id="answer-container-25339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25339-score" class="post-score" title="current number of votes">1</div><span id="post-25339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can see the Interface name in the Statistics-&gt;Summary, if you take a look at the first column of the list below the capture file comments. Wireshark does not show IP addresses or MACs for interfaces at the moment, at least as far as I can tell.</p><p>I've just updated <a href="http://www.tracewrangler.com">TraceWrangler</a> to show MAC and IP addresses in the PCAPng Structure Viewer, so if you run Windows somewhere you could use it to see them. Add your trace to the list, click on it, and select the "PCAPng Structure" Tab at the bottom.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/PCAPngStructView_1.png" alt="PCAPng Structure Viewer" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-25339" class="comments-container"><span id="25439"></span><div id="comment-25439" class="comment"><div id="post-25439-score" class="comment-score"></div><div class="comment-text"><ol><li>Interface name In the column you mention under Statistics-&gt;Summary, Wireshark shows the interface description (option if_description), not the name (option if_name). Wiresharks shows the interface name when there's no interface description in the PCAP-NG dump, it seems: Wireshark itself doesn't write any interface description (as you can check by opening a Wireshark dump with HexEdit or your TraceWrangler), so the Wireshark GUI shows the interface name; my program writes in a PCAP-NG dump file the interface name as well as an interface description, so the Wireshark GUI shows the interface description instead.</li><li>Addresses TraceWrangler works great, thanks. The only issue is, it shows the IPv4 address bytes in reverse order: i write in the PCAP-NG dump file 192 168 3 75 (in this byte order) and TraceWrangler shows "75.3.168.192"</li></ol></div><div id="comment-25439-info" class="comment-info"><span class="comment-age">(01 Oct '13, 01:39)</span> <span class="comment-user userinfo">ime-braun</span></div></div><span id="25447"></span><div id="comment-25447" class="comment"><div id="post-25447-score" class="comment-score"></div><div class="comment-text"><p>Hm, maybe I forgot to byte-swap the IP address, which would mean that I forgot it in two places - writing and reading the option :-) I'll have to check my code when I get home.</p><p>About the interface name - I didn't test yet what happens if both name and description are present, which is why I thought the name is in the summary.</p></div><div id="comment-25447-info" class="comment-info"><span class="comment-age">(01 Oct '13, 02:35)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="58089"></span><div id="comment-58089" class="comment"><div id="post-58089-score" class="comment-score"></div><div class="comment-text"><p>Is there a way to access these fields (section header , interface description) from plugin dissector code written in C?</p></div><div id="comment-58089-info" class="comment-info"><span class="comment-age">(14 Dec '16, 10:16)</span> <span class="comment-user userinfo">rashmi_s</span></div></div></div><div id="comment-tools-25339" class="comment-tools"></div><div class="clear"></div><div id="comment-25339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

