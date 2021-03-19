+++
type = "question"
title = "Track streaming from Netflix in near real time"
description = '''Hello, I have a question that might be a bit odd, so I will try to explain the application first. I have an object that I would like to change state depending on whether Netflix is being streamed or not. So when Netflix is not being streamed the system is in state A, when streaming starts it transit...'''
date = "2016-10-27T00:24:00Z"
lastmod = "2016-10-27T16:08:00Z"
weight = 56728
keywords = [ "streaming", "netflix" ]
aliases = [ "/questions/56728" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Track streaming from Netflix in near real time](/questions/56728/track-streaming-from-netflix-in-near-real-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56728-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a question that might be a bit odd, so I will try to explain the application first. I have an object that I would like to change state depending on whether Netflix is being streamed or not. So when Netflix is not being streamed the system is in state A, when streaming starts it transitions to state B and when streaming ends i returns to state A again. I would like it to occur in near real time (20-30 seconds after streaming has started/stopped).</p><p>I already have the system setup using Wireshark to monitor other network traffic, so I thought that perhaps it could be possible to utilize Wireshark for Netflix as well. But I am not a network wizard, which means that so far I have concluded that http requests to Netflix.com only occurs when loading the page initially and does not monitor streaming. A bit of research has made me understand that this is because Netflix actually get the content from multiple providers.</p><p>Does anyone have a good idea how to do this, or can tell me that it is in no way doable.</p></div><div id="question-tags" class="tags-container tags">streaming netflix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '16, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/af4751c9c9510d16a0cc089062b7c848?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nerq&#39;s gravatar image" /><p>Nerq<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nerq has no accepted answers">0%</span></p></div></div><div id="comments-container-56728" class="comments-container"></div><div id="comment-tools-56728" class="comment-tools"></div><div class="clear"></div><div id="comment-56728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56762"></span>

<div id="answer-container-56762" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56762-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It would mean using Wireshark to analyze the NetFlix traffic to see what would be distinctive for NetFlix traffic (which I have not done myself). Then when you do have discovered some display filter that will match the streaming packets (or just the requests for streams), you can use a while loop to detect the state like this:</p><pre><code>while true
do
    if [[ `-i &lt;int&gt; -a:5 -Y &lt;netflix-filter&gt; | wc -l | tr -d &quot; &quot;` == 0 ]]
    then
        echo &quot;State A&quot;
    else
        echo &quot;State B&quot;
    fi
done</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '16, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-56762" class="comments-container"><span id="56770"></span><div id="comment-56770" class="comment"><div id="post-56770-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer, I get the way to do it. I am just unsure how to configure the filter, I have identified the package requests and the return answers from the Netflix CDN. They look like this, but I am unsure how to filter them.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-10-28_at_09.18.24.png" alt="alt text" /></p></div><div id="comment-56770-info" class="comment-info"><span class="comment-age">(28 Oct '16, 00:23)</span> Nerq</div></div><span id="56772"></span><div id="comment-56772" class="comment"><div id="post-56772-score" class="comment-score"></div><div class="comment-text"><p>OK, I fired up NetFlix here in NL and made a trace. As the video streams are SSL encrypted, the only information you can go on are the IP addresses and the SSL handshake. In the SSL handshake, there is a SNI extension that you could filter on:</p><pre><code>$ tshark -r netflix.pcapng -Y &quot;ssl.handshake.extensions_server_name contains nflxvideo.net&quot;
10193  39.751633 0.000000 192.168.0.133 → ipv4_1-cxl0-c076.1.ams001.ix.nflxvideo.net SSL 296  64 Client Hello
10196  39.755777 0.004144 192.168.0.133 → ipv4_1-cxl0-c108.1.ams001.ix.nflxvideo.net SSL 296  64 Client Hello
10201  39.764074 0.008297 192.168.0.133 → ipv4_1-cxl0-c108.1.ams001.ix.nflxvideo.net SSL 296  64 Client Hello
10559  39.930507 0.166433 192.168.0.133 → ipv4_1-cxl0-c076.1.ams001.ix.nflxvideo.net SSL 583  64 Client Hello
11454  40.247803 0.317296 192.168.0.133 → ipv4_1-cxl0-c076.1.ams001.ix.nflxvideo.net SSL 583  64 Client Hello
11787  40.328245 0.080442 192.168.0.133 → ipv4_1-cxl0-c076.1.ams001.ix.nflxvideo.net SSL 583  64 Client Hello
11925  40.387909 0.059664 192.168.0.133 → ipv4_1-lagg0-c007.1.ams001.ix.nflxvideo.net SSL 297  64 Client Hello
11926  40.387987 0.000078 192.168.0.133 → ipv4_1-lagg0-c007.1.ams001.ix.nflxvideo.net SSL 297  64 Client Hello
20793  43.554383 3.166396 192.168.0.133 → ipv4_1-cxl0-c108.1.ams001.ix.nflxvideo.net SSL 583  64 Client Hello
$</code></pre><p>So you could use that, however, there are sessions that have very little data and sessions that do have data:</p><pre><code>$ for stream in `tshark -r netflix.pcapng -Y &quot;ssl.handshake.extensions_server_name contains nflxvideo.net&quot; -T fields -e tcp.stream`
do
    tshark -r netflix.pcapng -Y tcp.stream==$stream | wc -l
done
    2245
   26409
   28133
    1740
     165
      18
     251
      26
   20844
$</code></pre><p>Also, I only captured for 1-2 minutes, so I have no idea how often a new SLL session will be set up during the watching of a video stream. I will leave that to you to find out. Then you might need to do a two-step filter process. One to collect the destination IP addresses of the ClientHello messages and put them in a list. Then a second run on the capture to measure the amount of traffic towards these IP addresses.</p><p>Please note that I converted your "answer" to a "comment" as that is how this site works best, please see the FAQ for more details.</p></div><div id="comment-56772-info" class="comment-info"><span class="comment-age">(28 Oct '16, 01:06)</span> SYN-bit ♦♦</div></div><span id="56773"></span><div id="comment-56773" class="comment"><div id="post-56773-score" class="comment-score"></div><div class="comment-text"><p>Thanks for correcting my comment to an answer, and thanks for the reply.</p><p>I looked at the SSL and thought that it might not happen often enough, so instead I tried with a simple filter looking at the host of the source traffic. It looks like this:</p><pre><code>tshark -Y &quot;ip.src_host contains &quot;nflx&quot;&quot;</code></pre><p><code></code></p><code></code><p><code></code></p><p><code></code></p><p>And that actually works fairly well on my laptop giving me a lot of packages while streaming. But for some reason it does not work on the Raspberry Pi that I have setup to monitor traffic between my modem and router. It seems that the Raspberry is resolving the name into an IP for some reason (like I said I am not a networking wizard, so I have no idea why). I am looking into it, but so far I have only seen that the -n flag should not be set, and it is not.</p></div><div id="comment-56773-info" class="comment-info"><span class="comment-age">(28 Oct '16, 01:57)</span> Nerq</div></div><span id="56777"></span><div id="comment-56777" class="comment"><div id="post-56777-score" class="comment-score"></div><div class="comment-text"><p>Could you add <code>-o nameres.network_name:TRUE -o nameres.use_external_name_resolver:TRUE</code> to your tshark command to make sure name resolving is enabled?</p><p>You can look at the nameresolving settings that it is using without those two options with:</p><pre><code>$ tshark -G currentprefs | egrep &quot;^#?nameres&quot;
#nameres.mac_name: TRUE
#nameres.transport_name: FALSE
nameres.network_name: TRUE
#nameres.dns_pkt_addr_resolution: TRUE
#nameres.use_external_name_resolver: TRUE
#nameres.name_resolve_concurrency: 500
#nameres.hosts_file_handling: FALSE
#nameres.vlan_name: FALSE
#nameres.load_smi_modules: FALSE
#nameres.suppress_smi_errors: FALSE
$</code></pre></div><div id="comment-56777-info" class="comment-info"><span class="comment-age">(28 Oct '16, 02:09)</span> SYN-bit ♦♦</div></div><span id="56782"></span><div id="comment-56782" class="comment"><div id="post-56782-score" class="comment-score"></div><div class="comment-text"><p>I tried doing that, and I still get nothing showing up. The tshark command now looks like this</p><pre><code>sudo tshark -o nameres.network_name:TRUE -o nameres.use_external_name_resolver:TRUE -Y &quot;ip.src_host contains &quot;nflx&quot;&quot;</code></pre><p>Running the other tshark command yields me the following:</p><pre><code>#nameres.mac_name: TRUE
#nameres.transport_name: FALSE
#nameres.network_name: FALSE
#nameres.use_external_name_resolver: TRUE
#nameres.concurrent_dns: TRUE
#nameres.name_resolve_concurrency: 500
#nameres.hosts_file_handling: FALSE
#nameres.load_smi_modules: FALSE
#nameres.suppress_smi_errors: FALSE</code></pre><p><code></code></p><code></code><p><code></code></p><p><code></code></p><p>I talked with a colleague and he said that it probably likely that it is because the Raspberry is not the one doing the actual request, although I do not know if this is true.</p></div><div id="comment-56782-info" class="comment-info"><span class="comment-age">(28 Oct '16, 03:47)</span> Nerq</div></div><span id="56783"></span><div id="comment-56783" class="comment not_top_scorer"><div id="post-56783-score" class="comment-score"></div><div class="comment-text"><p>Maybe the Pi version of Tshark is not compiled with a name resolver? What is the output of <code>tshark -v</code>? And do you see name resolving for other IP's if you run <code>sudo tshark -o nameres.network_name:TRUE -o nameres.use_external_name_resolver:TRUE</code>? If you do not filter, do you see traffic to the NetFlix IP addresses coming by the Pi?</p></div><div id="comment-56783-info" class="comment-info"><span class="comment-age">(28 Oct '16, 04:16)</span> SYN-bit ♦♦</div></div><span id="56799"></span><div id="comment-56799" class="comment not_top_scorer"><div id="post-56799-score" class="comment-score"></div><div class="comment-text"><p>I found that the command will work</p><pre><code>sudo tshark -o nameres.network_name:TRUE -o nameres.use_external_name_resolver:TRUE -o nameres.transport_name:TRUE -Y &quot;ip.src_host contains &quot;nflx&quot;&quot;</code></pre><p><code></code></p><code></code><p><code></code></p><p><code></code></p><p>Thanks for guiding me in the right direction.</p></div><div id="comment-56799-info" class="comment-info"><span class="comment-age">(28 Oct '16, 23:44)</span> Nerq</div></div></div><div id="comment-tools-56762" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-56762-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

