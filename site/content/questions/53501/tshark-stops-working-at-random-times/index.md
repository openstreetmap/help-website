+++
type = "question"
title = "Tshark stops working at random times"
description = '''Hi All, First off, i am running Kali 2. on a Raspberry Pi 2b with a TP-Link TL-WN722N USB WiFi Dongle. Running tshark -v displays version 1.12.6 and running on Linux 3.18.16v7 with locale, with libpcap version 1.6.2 with libz 1.2.8. I hope that helps... So on to the problem. I ( myself and a buddy )...'''
date = "2016-06-16T12:11:00Z"
lastmod = "2016-06-19T14:07:00Z"
weight = 53501
keywords = [ "out-of-memory", "crash", "tshark", "linux" ]
aliases = [ "/questions/53501" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark stops working at random times](/questions/53501/tshark-stops-working-at-random-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53501-score" class="post-score" title="current number of votes">0</div><span id="post-53501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>First off, i am running Kali 2. on a Raspberry Pi 2b with a TP-Link TL-WN722N USB WiFi Dongle.</p><p>Running tshark -v displays version 1.12.6 and running on Linux 3.18.16v7 with locale, with libpcap version 1.6.2 with libz 1.2.8.</p><p>I hope that helps...</p><p>So on to the problem.</p><p>I ( myself and a buddy ) are trying to use the RPI to capture the number of wireless devices in a street for a study we are working on. Before anyone asks... yes i do have permission :-)</p><p>The RPI works great, it feeds the data back to a mini web portal we had written that displays the data graphically and on first boot up everything works great. ** disclaimer... We had quite a bit of help setting this up and unfortunately the guy helping has since moved on and no longer contactable.. hence the question here and also why parts of it may come across as being a noob... which we are to using Tshark / Wireshark.</p><p>After random periods the RPI stops sending data, we can log into it, ping the web server plus lots of other web related sites, the memory card is only around 30 % full... ( 16Gb in total ) and a memory check suggests there is plenty available... in essence everything seems fine.</p><p>If we stop and start Tshark service it makes no difference, we still do not receive any data. The only way to resolve it is to reboot the RPI.</p><p>Although i can not prove it i think the issue is related to the amount of data the RPI is receiving / sending. Reason being is throughout a night time the RPI lasts hours.. however on a normal day around lunch time when the street is at its busiest the data transmit stops and we have to reboot.</p><p>The command line we are running is as follows</p><pre><code>/usr/bin/nohup /usr/bin/tshark -l -I -i wlan1 -T fields -e frame.time_epoch -e wlan.sa -e radiotap.dbm_antsignal -e wlan_mgt.ssid -E occurrence=f type mgt subtype probe-req | /usr/bin/php /opt/dronecapture/tsharkparser.php&amp;</code></pre><p>The tsharkparser.php file the command line refers to is as follows</p><pre><code>&lt;?php
/*
This script parses the output from tshark command line

load the configuration file
*/
require(&#39;config.php&#39;);

/*
maybe we need to do some experimenting with this option.....?
*/
//stream_set_blocking(STDIN, 0);

while (false !== ($line = fgets(STDIN))) {
    $fields = preg_split(&#39;/\s+/&#39;, $line);

    /*
    we only process the data under certain conditions
    - valid mac address is submitted
    - transmission method is set to &quot;rest&quot;
    */
    if(filter_var($fields[1], FILTER_VALIDATE_MAC)) {
        /*
        POST a json message to a REST API
        - first assign the values collected from the probe request, to the vars
        */
        $ts     = $fields[0];
        $mac    = $fields[1];
        $rssi   = $fields[2];

        /*
        calculate the hash of the data to be submitted
        */
        $string_to_hash = $ts . &#39;|&#39; . $mac . &#39;|&#39; . $rssi . &#39;|&#39; . $drone_id . &#39;|&#39; . $public_key . &#39;|&#39; . $secret_key;
        $hash_of_string = sha1($string_to_hash);

        /*
        construct the json POST data to be submitted
        */
        $raw_data = array(&quot;ts&quot; =&gt; $ts, &quot;mac&quot; =&gt; $mac, &quot;rssi&quot; =&gt; $rssi, &quot;drone_id&quot; =&gt; $drone_id, &quot;public_key&quot; =&gt; $public_key, &quot;hash&quot; =&gt; $hash_of_string);
        $data_string = json_encode($raw_data);

        $ch = curl_init($probe_api_url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, &quot;POST&quot;);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            &#39;Content-Type: application/json&#39;,
            &#39;Content-Length: &#39; . strlen($data_string))
        );

        $result = curl_exec($ch);
    }
}
?&gt;</code></pre><p>I have read the articles re memory consumption ( <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">https://wiki.wireshark.org/KnownBugs/OutOfMemory</a> )and possibly switching to "dumpcap" but i have also read several questions on here from people with similar issues saying it makes no difference. Obviously as we are using an RPI i have no way to increase the physical RAM.</p><p>If anyone can offer any suggestions on what to do... at the moment i'm not even sure how to / if i can create a log file to find out whats happening i would really appreciate it.</p><p>In order to finish my study i need the RPI to run for around 4 days.. preferably a full week. At the moment i am having to reboot it 2 -3 times a day :-(</p><p>Many Thanks and apologies for such a long post.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-out-of-memory" rel="tag" title="see questions tagged &#39;out-of-memory&#39;">out-of-memory</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '16, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/73514d77c921e9443a1a3d4f425c2301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pigsfoot&#39;s gravatar image" /><p><span>Pigsfoot</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pigsfoot has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '16, 13:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53501" class="comments-container"><span id="53508"></span><div id="comment-53508" class="comment"><div id="post-53508-score" class="comment-score">1</div><div class="comment-text"><p>Okay, a lot of context, but what you basically say is that you loose reception on your wireless interface, which you can only recover by rebooting the Pi.</p><p>So, have a closer look at the wireless interface. Does the driver give out? Is it modular? Can you reload it?</p></div><div id="comment-53508-info" class="comment-info"><span class="comment-age">(16 Jun '16, 14:59)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53509"></span><div id="comment-53509" class="comment"><div id="post-53509-score" class="comment-score"></div><div class="comment-text"><p>Hi thanks for the reply. I can't be 100% certain but I don't think the issue is related to the adaptor or loosing reception. When we stop receiving data ... I. E. The rpi stops sending data to to our Web portal I have dropped and brought up the wlan interface and it makes no difference.</p><p>I have read more about simular problems and it's seems the issue that tshark may not be the right tool to use for long term scans when handling large amounts of data.</p><p>When we have managed to collect a good day of data, with several reboots we are seeing around 20,000 individual mac addresses... some of which multiple time as they go back and forth. As you can see from the script we run we send this data in real time to our Web server with 3 main segments. Mac address, rssi and a time stamp.</p><p>I hope this provides some more insight.</p><p>Thanks</p></div><div id="comment-53509-info" class="comment-info"><span class="comment-age">(16 Jun '16, 15:16)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53510"></span><div id="comment-53510" class="comment"><div id="post-53510-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>TP-Link TL-WN722N USB WiFi Dongle</p></blockquote></blockquote><p>I have several of these on an embedded Linux system to sniff channels 1/6/11, with the goal of 24/7 capture on a ring buffer with dumpcap. However, they routinely hang. Only recovery for me is to power cycle the device or remove/reinsert the USB adapter. However, I reboot as I also feed the data into a network manager and that likes to have the interface index constant, and resetting the USB device will index the SNMP interface index. So reboot it is...</p><p>I found Intel-based devices to have slightly better drivers than the ARM stuff.</p><p>For me, I put the interface into monitor mode then monitor the number of packets with ifconfig. Run ifconfig a couple of times and when the Rx packets does not change, it's hung. I wrote a shell script to automate this, but then my box can reset a lot. So I live without the data if it hangs and only use it as a best-effort back up source :(</p></div><div id="comment-53510-info" class="comment-info"><span class="comment-age">(16 Jun '16, 15:27)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="53515"></span><div id="comment-53515" class="comment"><div id="post-53515-score" class="comment-score"></div><div class="comment-text"><p><span>@Pigsfoot</span>: You're jumping to conclusions. ifdown/ifup doesn't help if the device or driver is in trouble. These are hardware/software underneath the interface you bring down and up. It won't necessary fix them.</p><p>Indeed dissection engines are prone to Out-Of-Memory (OOM) because they keep state. Using -1 option should alleviate that. If this is indeed a problem then should be able to pick up on that by monitoring memory usage during operations at daytime.</p><p>Setup the kernel OOM killer. That would kill tshark if it consumes ever more memory.</p><p>If it's tshark causing problems you should simply change your script. Have it relaunch every hour, stopping it from causing trouble.</p><p>So there are may options available, if your analysis is right.</p></div><div id="comment-53515-info" class="comment-info"><span class="comment-age">(16 Jun '16, 22:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53520"></span><div id="comment-53520" class="comment"><div id="post-53520-score" class="comment-score"></div><div class="comment-text"><p><span>@Jaap</span>: Thanks for the feedback, much appreciated. Thinking about what your saying does make some sense because when the web portal reports its not receiving any traffic i have logged into the RPI as per my original comment, checked the memory use and it would appear that i haven't ran out, i also restarted my capture script which didn't make any difference which kind of suggests it's not a memory issue at all.</p><p>I will however add the -1 option to my command line and also as suggested set up the OOM killer kernel just to see if it helps. I still think the issue is attributed to the amount of traffic being processed because on a quiet day / night time we have no issues, i just need to work out which bit is causing the problem :-). On the pus side the issue happens all the time during the day so i will know if its fixed it or not pretty quickly. If it continues to happen i will have to look into trying to do something with the wlan.... any suggestions ?</p><p>Thanks</p></div><div id="comment-53520-info" class="comment-info"><span class="comment-age">(17 Jun '16, 01:26)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53521"></span><div id="comment-53521" class="comment not_top_scorer"><div id="post-53521-score" class="comment-score"></div><div class="comment-text"><p>The RPI has actually stopped working this morning so i have just ran the following and and received the displayed responses</p><pre><code>[email protected]:~# free -m
             total       used       free     shared    buffers     cached
Mem:           744        245        499          5          9        168
-/+ buffers/cache:         67        677
Swap:            0          0          0

ps aux | grep tshark
root       362  0.0  7.1  97632 54544 ?        S    Jun16   0:17 /usr/bin/tshark -l -I -i wlan3 -T fields -e frame.time_epoch -e wlan.sa -e radiotap.dbm_antsignal -e wlan_mgt.ssid -E occurrence f type mgt subtype probe-req
root       363  0.0  1.7  37436 13076 ?        S    Jun16   0:18 /usr/bin/php /opt/dronecapture/tsharkparser.php
root      2823  0.0  0.0   2060   548 pts/0    S+   08:08   0:00 grep tshark</code></pre><p>Also</p><pre><code>systemctl status dronecapture.service -l
â dronecapture.service - Probe Request capture tool
Loaded: loaded (/lib/systemd/system/dronecapture.service; enabled)
Active: active (running) since Thu 2016-06-16 19:31:18 UTC; 12h ago
Process: 351 ExecStart=/opt/dronecapture/php-tshark.sh (code=exited, status=0/SUCCESS)
CGroup: /system.slice/dronecapture.service
       ââ362 /usr/bin/tshark -l -I -i wlan3 -T fields -e frame.time_epoch -e wlan.sa -e radiotap.dbm_antsignal -e wlan_mgt.ssid -E occurrence f type mgt subtype probe-req
       ââ363 /usr/bin/php /opt/dronecapture/tsharkparser.php
       ââ418 /usr/bin/dumpcap -n -i wlan3 -f type mgt subtype probe-req -I -Z none

Jun 16 19:31:18 DroneID23 systemd[1]: Started Probe Request capture tool.
Jun 16 19:31:23 DroneID23 php-tshark.sh[351]: tshark: Lua: Error during loading:
Jun 16 19:31:23 DroneID23 php-tshark.sh[351]: [string &quot;/usr/share/wireshark/init.lua&quot;]:46: dofile has been disabled due to running Wireshark as superuser. See     http://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user.
Jun 16 19:31:24 DroneID23 php-tshark.sh[351]: Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Jun 16 19:31:25 DroneID23 php-tshark.sh[351]: Capturing on &#39;wlan3&#39;</code></pre><p>Finally i ran - "systemctl restart dronecapture.service" which restarts the capture service and unfortunately it made no difference. The only way to bring the RPI back online is to reboot it.</p></div><div id="comment-53521-info" class="comment-info"><span class="comment-age">(17 Jun '16, 01:27)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53525"></span><div id="comment-53525" class="comment not_top_scorer"><div id="post-53525-score" class="comment-score"></div><div class="comment-text"><p>OKe, more post-mortem to do. Once the system fails, don't simply restart dronecapture, start looking at the wlan3 device. Look at system logs, see if anything pops. You could already look into the driver, see what options it provides to investigate further, and what's published on this combination on the PI2.</p><p>PS: Did you overclock this Pi? Might want to be careful with that as well.</p></div><div id="comment-53525-info" class="comment-info"><span class="comment-age">(17 Jun '16, 04:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53501" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-53501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53523"></span>

<div id="answer-container-53523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53523-score" class="post-score" title="current number of votes">1</div><span id="post-53523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think your system is failing due to hardware issues. It is likely throughput dependent: we can guess that whatever 'event' or specific scenario is causing the USB wifi adapter to fail is more likely to occur when more traffic is passed. I also recommend using tcpdump or dumpcap as the long term traffic collector, not one of the *sharks.</p><p>I have had better luck with these USB devices to do what you want:</p><p>Bus 002 Device 004: ID 0846:9012 NetGear, Inc. WNDA4100 802.11abgn 3x3:3 [Ralink RT3573]</p><p>In addition, they are more capable than the TP Link, but they cost more - I recall about $US40 on amazon.com, compared to $US13 for the TPLink. Make sure you use a recent kernel to get a good Ralink driver, but I don't know how that will work with the ARM chip. I moved away from ARM for these very reasons - to improve the quality of the Wifi captures on Linux. Note that these still crash, but I can get a couple of weeks out of them, instead of hours to days for the TP Link.</p><p>Example of system with Ralink wifi chips for packet capture:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RemoteCapture_-_Copy.jpg" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 02:57</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jun '16, 05:15</strong> </span></p></div></div><div id="comments-container-53523" class="comments-container"><span id="53524"></span><div id="comment-53524" class="comment"><div id="post-53524-score" class="comment-score"></div><div class="comment-text"><p>Hi Bob, That's very helpful thank you. So are you suggesting do away with the RPI and move to an Intel platform? I will get one of the WiFi adapters suggested and try that to see what difference it makes on the RPI.</p><p>I have had a look at a site i use and they offer a few Intel based alternatives to the RPI - <a href="http://uk.farnell.com/webapp/wcs/stores/servlet/Search?catalogId=15001&amp;langId=44&amp;storeId=10151&amp;categoryId=700000005178&amp;showResults=true&amp;aa=true&amp;sf=731&amp;pf=110181927">http://uk.farnell.com/webapp/wcs/stores/servlet/Search?catalogId=15001&amp;langId=44&amp;storeId=10151&amp;categoryId=700000005178&amp;showResults=true&amp;aa=true&amp;sf=731&amp;pf=110181927</a></p><p>Is there one there you would recommend or do you have a preferred platform you have tried?</p><p>One other question... if the issue is hardware related would having a script to drop and bring back up the wlan adapter on a regular basis make any difference? If not is there anything i can do short term while i try a different hardware platform.</p><p>Thanks</p></div><div id="comment-53524-info" class="comment-info"><span class="comment-age">(17 Jun '16, 04:49)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53526"></span><div id="comment-53526" class="comment"><div id="post-53526-score" class="comment-score"></div><div class="comment-text"><blockquote><blockquote><p>Is there one there you would recommend or do you have a preferred platform you have tried?</p></blockquote></blockquote><p>I have tried the Intel NUC and the Compulab stuff. I currently use the Compulab gear for 'spot' wifi captures with three+ USB NICs and have these distributed around the globe where I need them. I would attach a picture if I could, but I cannot to a comment.</p><p>I have had mixed success with cycling the adapter - I tried:</p><p>ifconfig wlanX down ifconfig wlanx up</p><p>and sometimes it works, but not always. There are several cases:</p><ol><li>No effect</li><li>Device comes back in monitor mode, but not in promiscuous mode anymore (i.e. only see broadcast/multicast now, until reboot)</li><li>Comes back fully until it crashes again...</li></ol><p>Result 2 is worst case - looks like it is up but it really isn't.</p><p>So I automated the checking of the adapters through ifconfig with cron/bash script but only reliable way to recover is a reboot. However, this was not true for the TP Link: a reboot did not always correct the issue - on some occasions I need to power cycle the USB device so I need to pull it from the socket, or kill power to the USB interface somehow. I would bet different systems handle power to usb bus differently.</p><p>I have Raspberry PIs, Udoo boards, Beagle boards. All cool, all cheap, but to get latest kernel with latest WiFi updates to improve stability, I moved to i386 embedded devices. YMMV.</p></div><div id="comment-53526-info" class="comment-info"><span class="comment-age">(17 Jun '16, 05:08)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="53527"></span><div id="comment-53527" class="comment"><div id="post-53527-score" class="comment-score"></div><div class="comment-text"><p><span>@Bob Jones</span>, the problem with pictures in comments is not so much how to post them but that in Comments, they are not auto-sized like in Questions and Answers so if you post them in the original (high) resolution, they make the whole page look ugly.</p><p>But you can edit your original answer and add the picture there. Or (pssst!) you can post another Answer with a picture in it and then convert it into a comment to another Answer - your karma should already allow that at least for your own Answers, but please first check whether the option "more -&gt; convert to comment" is available for your existing Answer.</p></div><div id="comment-53527-info" class="comment-info"><span class="comment-age">(17 Jun '16, 05:44)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="53531"></span><div id="comment-53531" class="comment"><div id="post-53531-score" class="comment-score"></div><div class="comment-text"><p>First things first... awesome forum... getting some great help on here. Thanks guys.</p><p>To start off with.. Nope the RPI 2b is straight out of the box.. not overclocked at all.</p><p>The RPI has just stopped working again so before a reboot i ran a couple of commands</p><p>This is where i start to suffer... I'm not really sure what to look for or how to get the Wlan logs...</p><p>I have just ran the following ... not sure if it is of any help</p><pre><code>[email protected]:~# dmesg | grep -i wlan3
[    5.539336] ath9k_htc 1-1.3:1.0 wlan3: renamed from wlan0
[    5.608374] systemd-udevd[160]: renamed network interface wlan0 to wlan3
[   21.144337] device wlan3 entered promiscuous mode
[    2.273783] usb 1-1.3: Product: USB2.0 WLAN
[    2.275528] usb 1-1.3: Manufacturer: ATHEROS
[    2.277204] usb 1-1.3: SerialNumber: 12345
[    4.513412] usb 1-1.3: ath9k_htc: Firmware htc_9271.fw requested
[    4.515626] usbcore: registered new interface driver ath9k_htc
[    4.818512] usb 1-1.3: ath9k_htc: Transferred FW: htc_9271.fw, size: 50980
Also, :- ifconfig shows this
wlan3     Link encap:UNSPEC  HWaddr F4-F2-6D-13-EC-41-30-30-00-00-00-00-00-00-00-00
          UP BROADCAST MULTICAST  MTU:1500  Metric:1
          RX packets:4945759 errors:0 dropped:8 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:1181209635 (1.1 GiB)  TX bytes:0 (0.0 B)</code></pre></code></pre></div><div id="comment-53531-info" class="comment-info"><span class="comment-age">(17 Jun '16, 06:33)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53532"></span><div id="comment-53532" class="comment not_top_scorer"><div id="post-53532-score" class="comment-score"></div><div class="comment-text"><p>I also ran this</p><pre><code>[email protected]:~# dmesg | grep -i usb
[    0.285161] usbcore: registered new interface driver usbfs
[    0.285293] usbcore: registered new interface driver hub
[    0.285461] usbcore: registered new device driver usb
[    0.414090] usbcore: registered new interface driver smsc95xx
[    0.843470] dwc_otg bcm2708_usb: DWC OTG Controller
[    0.845027] dwc_otg bcm2708_usb: new USB bus registered, assigned bus number 1
[    0.846612] dwc_otg bcm2708_usb: irq 32, io mem 0x00000000
[    0.851416] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002
[    0.852954] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
[    0.854479] usb usb1: Product: DWC OTG Controller
[    0.855967] usb usb1: Manufacturer: Linux 3.18.16-v7 dwc_otg_hcd
[    0.857493] usb usb1: SerialNumber: bcm2708_usb
[    0.859878] hub 1-0:1.0: USB hub found
[    0.863722] usbcore: registered new interface driver usb-storage
[    0.917692] usbcore: registered new interface driver usbhid
[    0.919294] usbhid: USB HID core driver
[    1.257587] usb 1-1: new high-speed USB device number 2 using dwc_otg
[    1.457889] usb 1-1: New USB device found, idVendor=0424, idProduct=9514
[    1.459777] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.462411] hub 1-1:1.0: USB hub found
[    1.737681] usb 1-1.1: new high-speed USB device number 3 using dwc_otg
[    1.840097] usb 1-1.1: New USB device found, idVendor=0424, idProduct=ec00
[    1.840110] usb 1-1.1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
[    1.911682] smsc95xx 1-1.1:1.0 eth0: register &#39;smsc95xx&#39; at usb-bcm2708_usb-1.1, smsc95xx USB 2.0 Ethernet, b8:27:eb:6d:19:c4
[    2.147844] usb 1-1.3: new high-speed USB device number 4 using dwc_otg
[    2.268382] usb 1-1.3: New USB device found, idVendor=0cf3, idProduct=9271
[    2.270269] usb 1-1.3: New USB device strings: Mfr=16, Product=32, SerialNumber=48
[    2.273783] usb 1-1.3: Product: USB2.0 WLAN
[    2.275528] usb 1-1.3: Manufacturer: ATHEROS
[    2.277204] usb 1-1.3: SerialNumber: 12345
[    4.513412] usb 1-1.3: ath9k_htc: Firmware htc_9271.fw requested
[    4.515626] usbcore: registered new interface driver ath9k_htc
[    4.818512] usb 1-1.3: ath9k_htc: Transferred FW: htc_9271.fw, size: 50980
[email protected]:~#</code></pre></div><div id="comment-53532-info" class="comment-info"><span class="comment-age">(17 Jun '16, 06:35)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53535"></span><div id="comment-53535" class="comment not_top_scorer"><div id="post-53535-score" class="comment-score"></div><div class="comment-text"><p>Have you polled <a href="http://raspberrypi.stackexchange.com/">StackExchange</a>?, because this is getting a bit out of scope.</p></div><div id="comment-53535-info" class="comment-info"><span class="comment-age">(17 Jun '16, 07:18)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="53536"></span><div id="comment-53536" class="comment"><div id="post-53536-score" class="comment-score">1</div><div class="comment-text"><p>Try:</p><p>iw dev</p><p>iwconfig</p><p>ifconfig (run multiple times, see if Rx packets is changing)</p><p>With WiFi, usually 2.4GHz is very busy so there are always networks out there and they beacon (usually) at ~100ms. So I typically expect to always see packets; even if the channel happens to be perfectly clear of networks, you should still catch probes now and again.</p></div><div id="comment-53536-info" class="comment-info"><span class="comment-age">(17 Jun '16, 07:56)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="53554"></span><div id="comment-53554" class="comment not_top_scorer"><div id="post-53554-score" class="comment-score"></div><div class="comment-text"><p>Hi, Based on suggestions of where the issue could be I have been looking into different Wireless adapters to try, I have an Alfa awus036nh, would that be better than the current TP-Link ? The Alfa range seems to be very popular in network sniffing and well supported for monitor mode.</p><p>Can anyone point me in the right direction on where to look within Linux to see if it is the wireless adapter that has stopped working.</p><p>Thanks</p></div><div id="comment-53554-info" class="comment-info"><span class="comment-age">(18 Jun '16, 08:04)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53561"></span><div id="comment-53561" class="comment not_top_scorer"><div id="post-53561-score" class="comment-score"></div><div class="comment-text"><p>Hi <span></span><span>@bob</span>-jones</p><p>Thanks for the feedback, thats just what i needed to know. I have done as suggested and when the drone goes "off line" as in the web portal reports its not receiving any traffic from the RPI i checked it and ran the ifconfig command several times and the RX packets are not changing. However if i do the same when it is working the number of packets change every time i run the command, literally one after the other.</p><p>I'm going to the Alfa AWUS036NH tomorrow and swap it out from the TP Link. From what i have read thats the better adapter and it uses a different chipset, on the plus side it shouldn't take long to see if it makes a difference. I have tried it on a spare RPI i have at home and it is recognized straight away when i plug it in so fingers crossed.</p><p>Thanks</p></div><div id="comment-53561-info" class="comment-info"><span class="comment-age">(19 Jun '16, 07:33)</span> <span class="comment-user userinfo">Pigsfoot</span></div></div><span id="53563"></span><div id="comment-53563" class="comment not_top_scorer"><div id="post-53563-score" class="comment-score"></div><div class="comment-text"><p>This is probably best continued on the RPi stack exchange site as <span>@Jaap</span> says. It's really a hardware/OS issue, not really a packet capture issue. I have better results with the RT chipsets so maybe the performance will better when you switch. Note they have issues too, so no guarantees.</p><p>Some points to move forward:</p><p><a href="https://lists.ath9k.org/mailman/listinfo/ath9k-devel">https://lists.ath9k.org/mailman/listinfo/ath9k-devel</a> <a href="https://wireless.wiki.kernel.org/en/users/drivers/ath9k">https://wireless.wiki.kernel.org/en/users/drivers/ath9k</a> <a href="https://wireless.wiki.kernel.org/en/users/drivers/ath9k/debug">https://wireless.wiki.kernel.org/en/users/drivers/ath9k/debug</a></p></div><div id="comment-53563-info" class="comment-info"><span class="comment-age">(19 Jun '16, 10:46)</span> <span class="comment-user userinfo">Bob Jones</span></div></div></div><div id="comment-tools-53523" class="comment-tools"><span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a></div><div class="clear"></div><div id="comment-53523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53565"></span>

<div id="answer-container-53565" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53565-score" class="post-score" title="current number of votes">0</div><span id="post-53565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for all your help guys... at least i know where to concentrate my efforts now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '16, 14:07</strong></p><img src="https://secure.gravatar.com/avatar/73514d77c921e9443a1a3d4f425c2301?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pigsfoot&#39;s gravatar image" /><p><span>Pigsfoot</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pigsfoot has no accepted answers">0%</span></p></div></div><div id="comments-container-53565" class="comments-container"></div><div id="comment-tools-53565" class="comment-tools"></div><div class="clear"></div><div id="comment-53565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

