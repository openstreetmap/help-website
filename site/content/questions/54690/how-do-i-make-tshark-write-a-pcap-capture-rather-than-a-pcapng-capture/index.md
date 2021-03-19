+++
type = "question"
title = "How do I make tshark write a pcap capture rather than a pcapng capture?"
description = '''I&#x27;m using tshark to capture network traffic as pcap file but when the dumping is done the captured file format is pcapng at the end! I don&#x27;t know what is the problem! I use this command in my Linux shell: sudo tshark -i eth0 -w test.pcap -F pcap'''
date = "2016-08-09T02:57:00Z"
lastmod = "2016-08-09T03:06:00Z"
weight = 54690
keywords = [ "file-format", "pcap", "tshark" ]
aliases = [ "/questions/54690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I make tshark write a pcap capture rather than a pcapng capture?](/questions/54690/how-do-i-make-tshark-write-a-pcap-capture-rather-than-a-pcapng-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark to capture network traffic as pcap file but when the dumping is done the captured file format is pcapng at the end! I don't know what is the problem! I use this command in my Linux shell:<br />
<em>sudo tshark -i eth0 -w test.pcap -F pcap</em></p></div><div id="question-tags" class="tags-container tags">file-format pcap tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Aug '16, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/69a28419552e24af6e1e7ae8c6159f2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="met1366&#39;s gravatar image" /><p>met1366<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="met1366 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Aug '16, 21:25</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-54690" class="comments-container"></div><div id="comment-tools-54690" class="comment-tools"></div><div class="clear"></div><div id="comment-54690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54691"></span>

<div id="answer-container-54691" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54691-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to specify <strong>libpcap</strong> as -F parameter:</p><p><code>sudo tshark -i eth0 -w test.pcap -F libpcap</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Aug '16, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54691" class="comments-container"><span id="54693"></span><div id="comment-54693" class="comment"><div id="post-54693-score" class="comment-score"></div><div class="comment-text"><p>Hmm. <code>tshark -F</code> shows the options, and for a master build I get:</p><pre><code>PS C:\&gt; &amp; &#39;C:\Program Files\Wireshark\tshark.exe&#39; -F                     
C:\Program Files\Wireshark\tshark.exe: option requires an argument -- &#39;F&#39;
tshark: The available capture file types for the &quot;-F&quot; flag are:          
    5views - InfoVista 5View capture                                     
    btsnoop - Symbian OS btsnoop                                         
    commview - TamoSoft CommView                                         
    dct2000 - Catapult DCT2000 trace (.out format)                       
    erf - Endace ERF capture                                             
    eyesdn - EyeSDN USB S0/E1 ISDN trace format                          
    k12text - K12 text file                                              
    lanalyzer - Novell LANalyzer                                         
    logcat - Android Logcat Binary format                                
    logcat-brief - Android Logcat Brief text format                      
    logcat-long - Android Logcat Long text format                        
    logcat-process - Android Logcat Process text format                  
    logcat-tag - Android Logcat Tag text format                          
    logcat-thread - Android Logcat Thread text format                    
    logcat-threadtime - Android Logcat Threadtime text format            
    logcat-time - Android Logcat Time text format                        
    modlibpcap - Modified tcpdump - libpcap                              
    netmon1 - Microsoft NetMon 1.x                                       
    netmon2 - Microsoft NetMon 2.x                                       
    nettl - HP-UX nettl trace                                            
    ngsniffer - Sniffer (DOS)                                            
    ngwsniffer_1_1 - NetXray, Sniffer (Windows) 1.1                      
    ngwsniffer_2_0 - Sniffer (Windows) 2.00x                             
    niobserver - Network Instruments Observer                            
    nokialibpcap - Nokia tcpdump - libpcap                               
    nseclibpcap - Wireshark - nanosecond libpcap                         
    nstrace10 - NetScaler Trace (Version 1.0)                            
    nstrace20 - NetScaler Trace (Version 2.0)                            
    nstrace30 - NetScaler Trace (Version 3.0)                            
    nstrace35 - NetScaler Trace (Version 3.5)                            
    pcap - Wireshark/tcpdump/... - pcap                                  
    pcapng - Wireshark/... - pcapng                                      
    rf5 - Tektronix K12xx 32-bit .rf5 format                             
    rh6_1libpcap - RedHat 6.1 tcpdump - libpcap                          
    snoop - Sun snoop                                                    
    suse6_3libpcap - SuSE 6.3 tcpdump - libpcap                          
    visual - Visual Networks traffic capture</code></pre></div><div id="comment-54693-info" class="comment-info"><span class="comment-age">(09 Aug '16, 03:21)</span> grahamb ♦</div></div><span id="54694"></span><div id="comment-54694" class="comment"><div id="post-54694-score" class="comment-score"></div><div class="comment-text"><p>Interesting - you're right, same for me. I always use "libpcap" and it still seems to work. But "pcap" also works. I think older versions only had "libpcap" as parameter option.</p><p>So maybe @met1366 needs to upgrade his tshark binaries.</p></div><div id="comment-54694-info" class="comment-info"><span class="comment-age">(09 Aug '16, 03:27)</span> Jasper ♦♦</div></div><span id="54697"></span><div id="comment-54697" class="comment"><div id="post-54697-score" class="comment-score"></div><div class="comment-text"><p>The problem was I had tshark version 1.10.6 which had a bug not to capture pcap file! I've already upgraded to latest version and now it's fixed.<br />
Thanks</p></div><div id="comment-54697-info" class="comment-info"><span class="comment-age">(09 Aug '16, 04:36)</span> met1366</div></div><span id="54705"></span><div id="comment-54705" class="comment"><div id="post-54705-score" class="comment-score">1</div><div class="comment-text"><p>You can use either pcap or libpcap since <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=commitdiff;h=a4ad9e9f74d58f3a869ceb27845f74345d7b81be">this</a> commit.</p></div><div id="comment-54705-info" class="comment-info"><span class="comment-age">(09 Aug '16, 09:24)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-54691" class="comment-tools"></div><div class="clear"></div><div id="comment-54691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

