+++
type = "question"
title = "Waitpid() error starting"
description = '''Hi, I&#x27;m running the latest 1.99 OSX version of Wireshark on OSX 10.10 Yosemite than ran fine until yesterday. All of a sudden I get the following error: Error from waitpid(): Interrupted system call. I completely uninstalled and reinstalled. Exactly 1 time I found an interface; second time:none! Can...'''
date = "2014-06-23T01:24:00Z"
lastmod = "2015-02-21T01:08:00Z"
weight = 34057
keywords = [ "wireshark" ]
aliases = [ "/questions/34057" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Waitpid() error starting](/questions/34057/waitpid-error-starting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34057-score" class="post-score" title="current number of votes">2</div><span id="post-34057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm running the latest 1.99 OSX version of Wireshark on OSX 10.10 Yosemite than ran fine until yesterday. All of a sudden I get the following error:</p><p>Error from waitpid(): Interrupted system call.</p><p>I completely uninstalled and reinstalled. Exactly 1 time I found an interface; second time:none!</p><p>Can you help Kind regards, Loe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '14, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/bbba1b5736eafd024fe8d8a4325807db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Loe%20Walter&#39;s gravatar image" /><p><span>Loe Walter</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Loe Walter has no accepted answers">0%</span></p></div></div><div id="comments-container-34057" class="comments-container"><span id="34199"></span><div id="comment-34199" class="comment"><div id="post-34199-score" class="comment-score"></div><div class="comment-text"><p>Same thing here... that error means the interfaces can't be found. I checked and ChmodBPF is not installed. I am not sure, but it looks like a permissions thing is preventing proper install of Wireshark 1.99 (earlier versions don't even load to the main screen).</p><p>marc</p></div><div id="comment-34199-info" class="comment-info"><span class="comment-age">(25 Jun '14, 18:30)</span> <span class="comment-user userinfo">Marc Abrams</span></div></div><span id="34200"></span><div id="comment-34200" class="comment"><div id="post-34200-score" class="comment-score"></div><div class="comment-text"><p>"ChmodBPF is not installed". I.e., if you do</p><pre><code>sudo launchctl list | egrep ChmodBPF</code></pre><p>it doesn't print</p><pre><code>-       0       org.wireshark.ChmodBPF</code></pre><p>?</p></div><div id="comment-34200-info" class="comment-info"><span class="comment-age">(25 Jun '14, 18:56)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34202"></span><div id="comment-34202" class="comment"><div id="post-34202-score" class="comment-score"></div><div class="comment-text"><p>Hi, Gary:</p><p>It DOES show it:</p><pre><code>Last login: Wed Jun 25 18:25:12 on ttys000
Marcs-MacBook-Pro:~ marc$ sudo launchctl list | egrep ChmodBPF
Password:
-   0   org.wireshark.ChmodBPF
Marcs-MacBook-Pro:~ marc$</code></pre><p>But the interfaces still don't show up in the app.</p><p>Thanks.</p><p>marc</p></div><div id="comment-34202-info" class="comment-info"><span class="comment-age">(25 Jun '14, 19:07)</span> <span class="comment-user userinfo">Marc Abrams</span></div></div><span id="34203"></span><div id="comment-34203" class="comment"><div id="post-34203-score" class="comment-score"></div><div class="comment-text"><p>So what does <code>ls -l /dev/bpf*</code> print?</p></div><div id="comment-34203-info" class="comment-info"><span class="comment-age">(25 Jun '14, 19:12)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34205"></span><div id="comment-34205" class="comment"><div id="post-34205-score" class="comment-score"></div><div class="comment-text"><p>Hi, Gary:</p><p>See:</p><pre><code>Marcs-MacBook-Pro:~ marc$ ls -l /dev/bpf* 
crw-rw----  1 root  access_bpf   23,   0 Jun 25 20:02 /dev/bpf0
crw-rw----  1 root  access_bpf   23,   1 Jun 25 20:02 /dev/bpf1
crw-rw----  1 root  access_bpf   23,  10 Jun 25 20:02 /dev/bpf10</code></pre><p>(other lines with the same permissions, owner, and group omitted)</p><pre><code>crw-rw----  1 root  access_bpf   23,  99 Jun 25 20:02 /dev/bpf99
Marcs-MacBook-Pro:~ marc$</code></pre><p>Thanks.</p><p>marc.</p></div><div id="comment-34205-info" class="comment-info"><span class="comment-age">(25 Jun '14, 20:08)</span> <span class="comment-user userinfo">Marc Abrams</span></div></div><span id="34206"></span><div id="comment-34206" class="comment not_top_scorer"><div id="post-34206-score" class="comment-score"></div><div class="comment-text"><p>So ChmodBPF <em>is</em> installed and it <em>is</em> doing what it's supposed to do (you have a ton of BPF devices, all with rw-rw---- permissions, and all owned by the access_bpf group).</p><p>What does the command <code>id</code> print?</p></div><div id="comment-34206-info" class="comment-info"><span class="comment-age">(25 Jun '14, 20:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34234"></span><div id="comment-34234" class="comment not_top_scorer"><div id="post-34234-score" class="comment-score"></div><div class="comment-text"><p>Hi, Gary:</p><p>I made myself root and launched Wireshark from the terminal and I see that it cannot capture the interfaces:</p><p>16:37:18.211 Capture Msg Capture Interface List failed!</p><p>Not sure what to do from here.</p><p>marc.</p></div><div id="comment-34234-info" class="comment-info"><span class="comment-age">(26 Jun '14, 16:46)</span> <span class="comment-user userinfo">Marc Abrams</span></div></div><span id="34236"></span><div id="comment-34236" class="comment not_top_scorer"><div id="post-34236-score" class="comment-score"></div><div class="comment-text"><p>Hi Gary,</p><p>Can you come to some kind of conclusion when reading this:</p><pre><code>sh-3.2# ./Wireshark
 2014-06-27 09:43:52.577 Wireshark[1841:907457] TSplicedFont failed creating descriptor for:
(
        {
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7ff2d35e5620&gt;&quot;;
        name = &quot;.STHeitiUISC-Thin&quot;;
    }
)
 2014-06-27 09:43:52.580 Wireshark[1841:907457] TSplicedFont failed creating descriptor for:
(
        {
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7ff2d35e5620&gt;&quot;;
        name = &quot;.STHeitiUITC-Thin&quot;;
    }
)
 2014-06-27 09:43:52.580 Wireshark[1841:907457] TSplicedFont failed creating descriptor for:
(
        {
        NSCTFontFeatureSettingsAttribute =         (
                        {
                CTFeatureSelectorIdentifier = 8;
                CTFeatureTypeIdentifier = 22;
            }
        );
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7ff2d5a19c20&gt;&quot;;
        name = &quot;.HiraKakuInterface-W2&quot;;
    }
)
 FIX: packet list heading menu sensitivity 
 09:43:56.777  Dbg  plugin_dir: /Applications/Wireshark.app/Contents/PlugIns/wireshark
 09:43:56.837 Main Dbg  Translator nl_NL
 09:43:56.837  Dbg  FIX: timestamp types should be set elsewhere
 09:43:56.837 Main Info fill_in_local_interfaces() starts
 09:43:56.837 Capture Msg  Capture Interface List ...
 09:43:56.837 Capture Dbg  sync_interface_list_open
 09:43:56.837 Capture Dbg  sync_pipe_open_command
 09:43:57.009 Capture Dbg  read 17 indicator: S empty value
 09:43:57.010 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.010 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,001s
 09:43:57.010 Capture Msg  Capture Interface Capabilities ...
 09:43:57.010 Capture Dbg  sync_if_capabilities_open
 09:43:57.010 Capture Dbg  sync_pipe_open_command
 09:43:57.019 Capture Dbg  read 17 indicator: S empty value
 09:43:57.019 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.019 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.019 Capture Msg  Capture Interface Capabilities failed!
 09:43:57.020 Capture Msg  Capture Interface Capabilities ...
 09:43:57.020 Capture Dbg  sync_if_capabilities_open
 09:43:57.020 Capture Dbg  sync_pipe_open_command
 09:43:57.028 Capture Dbg  read 17 indicator: S empty value
 09:43:57.028 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.028 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.028 Capture Msg  Capture Interface Capabilities ...
 09:43:57.028 Capture Dbg  sync_if_capabilities_open
 09:43:57.029 Capture Dbg  sync_pipe_open_command
 09:43:57.037 Capture Dbg  read 17 indicator: S empty value
 09:43:57.038 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.038 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.038 Capture Msg  Capture Interface Capabilities ...
 09:43:57.038 Capture Dbg  sync_if_capabilities_open
 09:43:57.038 Capture Dbg  sync_pipe_open_command
 09:43:57.046 Capture Dbg  read 17 indicator: S empty value
 09:43:57.047 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.047 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.047 Capture Msg  Capture Interface Capabilities ...
 09:43:57.047 Capture Dbg  sync_if_capabilities_open
 09:43:57.047 Capture Dbg  sync_pipe_open_command
 09:43:57.056 Capture Dbg  read 17 indicator: S empty value
 09:43:57.056 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.057 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.057 Capture Msg  Capture Interface Capabilities ...
 09:43:57.057 Capture Dbg  sync_if_capabilities_open
 09:43:57.057 Capture Dbg  sync_pipe_open_command
 09:43:57.065 Capture Dbg  read 17 indicator: S empty value
 09:43:57.066 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.066 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.066 Capture Msg  Capture Interface Capabilities ...
 09:43:57.066 Capture Dbg  sync_if_capabilities_open
 09:43:57.066 Capture Dbg  sync_pipe_open_command
 09:43:57.074 Capture Dbg  read 17 indicator: S empty value
 09:43:57.075 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.075 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.075 Capture Msg  Capture Interface Capabilities ...
 09:43:57.075 Capture Dbg  sync_if_capabilities_open
 09:43:57.075 Capture Dbg  sync_pipe_open_command
 09:43:57.083 Capture Dbg  read 17 indicator: S empty value
 09:43:57.083 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.084 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,000s
 09:43:57.084 Main Info fill_in_local_interfaces() ends, taking 0,246s
 09:43:57.085  Dbg  FIX: fetch recent color settings
 09:43:57.086 Capture Msg  Capture Interface List ...
 09:43:57.086 Capture Dbg  sync_interface_list_open
 09:43:57.086 Capture Dbg  sync_pipe_open_command
 09:43:57.151 Capture Dbg  read 17 indicator: S empty value
 09:43:57.151 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
 09:43:57.152 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0,001s
 09:43:57.152 Capture Msg  Capture Interface List failed!
 09:43:57.164 Main Info Wireshark is up and ready to go</code></pre><p>Thanks again</p></div><div id="comment-34236-info" class="comment-info"><span class="comment-age">(27 Jun '14, 00:46)</span> <span class="comment-user userinfo">Loe Walter</span></div></div><span id="34237"></span><div id="comment-34237" class="comment not_top_scorer"><div id="post-34237-score" class="comment-score"></div><div class="comment-text"><p>Even stranger Gary... When opening Menu-&gt; Capture -&gt; Interfaces</p><p>I can see ALL interfaces and can even start en1 (Wireless)</p><p>Strange isn't it?</p><p>Loe</p></div><div id="comment-34237-info" class="comment-info"><span class="comment-age">(27 Jun '14, 00:49)</span> <span class="comment-user userinfo">Loe Walter</span></div></div><span id="34238"></span><div id="comment-34238" class="comment not_top_scorer"><div id="post-34238-score" class="comment-score"></div><div class="comment-text"><p>And now for something completely different.... I close Wireshark and start it again from the console. Same errors as earlier, but NO interfaces anymore....????</p><p>Loe</p></div><div id="comment-34238-info" class="comment-info"><span class="comment-age">(27 Jun '14, 00:54)</span> <span class="comment-user userinfo">Loe Walter</span></div></div><span id="34253"></span><div id="comment-34253" class="comment not_top_scorer"><div id="post-34253-score" class="comment-score"></div><div class="comment-text"><p>The only conclusion I can come to is that Wireshark isn't logging enough information to come to any more detailed conclusion. Try downloading the latest build from <a href="http://www.wireshark.org/download/automated/osx/">the OS X automated build directory</a> and see what that does and what that logs; I changed the code to log more details on "Capture Interface Capabilities failed!" failures.</p></div><div id="comment-34253-info" class="comment-info"><span class="comment-age">(27 Jun '14, 14:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="34451"></span><div id="comment-34451" class="comment not_top_scorer"><div id="post-34451-score" class="comment-score"></div><div class="comment-text"><p>Using the latest build in the automated build directory (g4ac9895) I am having the same issue, my logs also look almost identical:</p><pre><code>$ wireshark
2014-07-07 09:45:49.988 Wireshark[16052:543970] TSplicedFont failed creating descriptor for:
(
        {
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7fb9d9e95620&gt;&quot;;
        name = &quot;.STHeitiUISC-Thin&quot;;
    }
)
2014-07-07 09:45:49.991 Wireshark[16052:543970] TSplicedFont failed creating descriptor for:
(
        {
        NSCTFontFeatureSettingsAttribute =         (
                        {
                CTFeatureSelectorIdentifier = 8;
                CTFeatureTypeIdentifier = 22;
            }
        );
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7fb9d9df43a0&gt;&quot;;
        name = &quot;.HiraKakuInterface-W2&quot;;
    }
)
2014-07-07 09:45:49.992 Wireshark[16052:543970] TSplicedFont failed creating descriptor for:
(
        {
        UnicodeCharSetTrim = &quot;&lt;__NSCFCharacterSet: 0x7fb9d9e95620&gt;&quot;;
        name = &quot;.STHeitiUITC-Thin&quot;;
    }
)
FIX: packet list heading menu sensitivity 
09:45:50.906  Dbg  plugin_dir: /Applications/Wireshark.app/Contents/PlugIns/wireshark
09:45:50.931 Main Dbg  Translator en_CA
09:45:50.932  Dbg  FIX: timestamp types should be set elsewhere
09:45:50.932 Main Info fill_in_local_interfaces() starts
09:45:50.932 Capture Msg  Capture Interface List ...
09:45:50.932 Capture Dbg  sync_interface_list_open
09:45:50.932 Capture Dbg  sync_pipe_open_command
09:45:51.010 Capture Dbg  read 19 indicator: S empty value
09:45:51.011 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
09:45:51.012 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.001s
09:45:51.012 Capture Msg  Capture Interface List failed, error 32767, Error from waitpid(): Interrupted system call (no secondary message)!
09:45:51.012 Main Info fill_in_local_interfaces() ends, taking 0.080s
09:45:51.015  Dbg  FIX: fetch recent color settings
09:45:51.016 Capture Msg  Capture Interface List ...
09:45:51.016 Capture Dbg  sync_interface_list_open
09:45:51.016 Capture Dbg  sync_pipe_open_command
09:45:51.092 Capture Dbg  read 19 indicator: S empty value
09:45:51.093 Capture Dbg  sync_pipe_wait_for_child: wait till child closed
09:45:51.093 Capture Dbg  sync_pipe_wait_for_child: capture child closed after 0.001s
09:45:51.094 Capture Msg  Capture Interface List failed, error 0, Error from waitpid(): Interrupted system call (no secondary message)!
09:45:51.105 Main Info Wireshark is up and ready to go</code></pre><p>Rolling back to 1.10.8 (32Bit) does not exhibit the issue.</p></div><div id="comment-34451-info" class="comment-info"><span class="comment-age">(07 Jul '14, 08:59)</span> <span class="comment-user userinfo">ericyanush</span></div></div></div><div id="comment-tools-34057" class="comment-tools"><span class="comments-showing"> showing 5 of 12 </span> <a href="#" class="show-all-comments-link">show 7 more comments</a></div><div class="clear"></div><div id="comment-34057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37290"></span>

<div id="answer-container-37290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37290-score" class="post-score" title="current number of votes">2</div><span id="post-37290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to get around this by adding myself to the access_bpf group.</p><pre><code>sudo dseditgroup -o edit -a myusername -t user access_bpf</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/02d5992f259c3a117f1dbfb32930f512?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amoeba&#39;s gravatar image" /><p><span>Amoeba</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amoeba has no accepted answers">0%</span></p></div></div><div id="comments-container-37290" class="comments-container"><span id="37299"></span><div id="comment-37299" class="comment"><div id="post-37299-score" class="comment-score"></div><div class="comment-text"><p>Confirmed to fix the same issue in my environment.</p></div><div id="comment-37299-info" class="comment-info"><span class="comment-age">(22 Oct '14, 20:10)</span> <span class="comment-user userinfo">MagnusMortensen</span></div></div></div><div id="comment-tools-37290" class="comment-tools"></div><div class="clear"></div><div id="comment-37290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39981"></span>

<div id="answer-container-39981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39981-score" class="post-score" title="current number of votes">0</div><span id="post-39981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe you can check for EINTR and try again for waitpid(). A waitpid with WNOHANG can return for any number of reasons causing interrupted syscall.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '15, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/07af62347225e0065448c09ed44c6687?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws_fan_2014&#39;s gravatar image" /><p><span>ws_fan_2014</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws_fan_2014 has no accepted answers">0%</span></p></div></div><div id="comments-container-39981" class="comments-container"><span id="39997"></span><div id="comment-39997" class="comment"><div id="post-39997-score" class="comment-score"></div><div class="comment-text"><p>Here is a diff that I verified works on my MacBook Pro running Yosemite.</p><pre><code>diff --git a/capchild/capture_sync.c b/capchild/capture_sync.c
index 55be896..54ec8c1 100644
--- a/capchild/capture_sync.c
+++ b/capchild/capture_sync.c
@@ -1865,7 +1865,8 @@ static int
 sync_pipe_wait_for_child(int fork_child, gchar msgp)
 {
     int fork_child_status;
-    int ret;
+    int retry_waitpid = 3;
+    int ret = -1;
     GTimeVal start_time;
     GTimeVal end_time;
     float elapsed;
@@ -1898,6 +1899,7 @@ sync_pipe_wait_for_child(int fork_child, gchar msgp)
         }
     }
 #else
+    while (--retry_waitpid &gt;= 0) {
         if (waitpid(fork_child, &amp;fork_child_status, 0) != -1) {
             if (WIFEXITED(fork_child_status)) {
                 /
@@ -1923,6 +1925,10 @@ sync_pipe_wait_for_child(int fork_child, gchar msgp)
                                         fork_child_status);
                 ret = -1;
             }
+
+        } else if (errno == EINTR) {
+            g_log(LOG_DOMAIN_CAPTURE, G_LOG_LEVEL_WARNING, &quot;sync_pipe_wait_for_child: waitpid returned EINTR. retrying.&quot;);
+            continue;
         } else if (errno != ECHILD) {
             *msgp = g_strdup_printf(&quot;Error from waitpid(): %s&quot;, g_strerror(errno));
             ret = -1;
@@ -1930,6 +1936,8 @@ sync_pipe_wait_for_child(int fork_child, gchar msgp)
             / errno == ECHILD ; echld might have already reaped the child */
             ret = fetch_dumpcap_pid ? 0 : -1;
         }
+        break;
+    }
 #endif
 g_get_current_time(&amp;end_time);</code></pre></pre></div><div id="comment-39997-info" class="comment-info"><span class="comment-age">(20 Feb '15, 16:11)</span> <span class="comment-user userinfo">ws_fan_2014</span></div></div><span id="40000"></span><div id="comment-40000" class="comment"><div id="post-40000-score" class="comment-score"></div><div class="comment-text"><p>While it can be difficult to determine if an issue is user-based, environment-based or a bug so all are fair game for Ask Wireshark, actual bugs should go to the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, and patches should follow the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html">Submission Guide</a> and go into the <a href="https://code.wireshark.org/review">Wireshark Gerrit</a> system for review.</p></div><div id="comment-40000-info" class="comment-info"><span class="comment-age">(21 Feb '15, 01:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-39981" class="comment-tools"></div><div class="clear"></div><div id="comment-39981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

