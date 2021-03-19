+++
type = "question"
title = "Windows Eventid 129 error"
description = '''Hi, We&#x27;ve set up Wireshark on a Windows 7 pro machine. It is connected to a layer 3 Cisco switch and we are using it to look at all packets. I was checking the event logs and noted that since it was put in place it has been logging the following events for all PC&#x27;s connected to the switch: Log Name:...'''
date = "2015-01-20T08:53:00Z"
lastmod = "2015-01-20T09:21:00Z"
weight = 39317
keywords = [ "windows", "configuration", "error129" ]
aliases = [ "/questions/39317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows Eventid 129 error](/questions/39317/windows-eventid-129-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39317-score" class="post-score" title="current number of votes">0</div><span id="post-39317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We've set up Wireshark on a Windows 7 pro machine. It is connected to a layer 3 Cisco switch and we are using it to look at all packets. I was checking the event logs and noted that since it was put in place it has been logging the following events for all PC's connected to the switch:</p><pre><code>Log Name:      Microsoft-Windows-WinRM/Operational   Source:        Microsoft-Windows-WinRM
Date:          1/20/2015 9:45:36 AM  Event ID:      80   Task Category: Request handling
Level:         Information   Keywords:      Client   User:          NETWORK SERVICE
Computer:      Shark.local
Description:   Sending the request for operation Subscription to destination machine and pc.local:5985
Event Xml: &lt;Event xmlns=&quot;http://schemas.microsoft.com/win/2004/08/events/event&quot;&gt;
  &lt;System&gt;     &lt;Provider Name=&quot;Microsoft-Windows-WinRM&quot; Guid=&quot;{A7975C8F-AC13-49F1-87DA-5A984A4AB417}&quot; /&gt;     &lt;EventID&gt;80&lt;/EventID&gt;      &lt;Version&gt;0&lt;/Version&gt;      &lt;Level&gt;4&lt;/Level&gt;
    &lt;Task&gt;9&lt;/Task&gt;    &lt;Opcode&gt;1&lt;/Opcode&gt;     &lt;Keywords&gt;0x4000000000000002&lt;/Keywords&gt;
    &lt;TimeCreated SystemTime=&quot;2015-01-20T14:45:36.679879800Z&quot; /&gt;
    &lt;EventRecordID&gt;108886&lt;/EventRecordID&gt;
    &lt;Correlation ActivityID=&quot;{02D14C50-F800-0002-7BBA-24BE3931D001}&quot; /&gt;
    &lt;Execution ProcessID=&quot;1016&quot; ThreadID=&quot;1548&quot; /&gt;
    &lt;Channel&gt;Microsoft-Windows-WinRM/Operational&lt;/Channel&gt;
    &lt;Computer&gt;Shark.LOCAL&lt;/Computer&gt;    &lt;Security UserID=&quot;S-1-5-20&quot; /&gt;  &lt;EventData&gt;
    &lt;Data Name=&quot;operationName&quot;&gt;Subscription&lt;/Data&gt;    &lt;Data Name=&quot;url&quot;&gt;.local&lt;/Data&gt;
    &lt;Data Name=&quot;port&quot;&gt;5985&lt;/Data&gt;

Log Name:      Microsoft-Windows-WinRM/Operational  Source:        Microsoft-Windows-WinRM
Date:          1/20/2015 9:45:36 AM    Event ID:      166   Task Category: User authentication
Level:         Information   Keywords:      Security,Client      User:          NETWORK SERVICE
Computer:      Shark.LOCAL
Description:  The chosen authentication mechanism is Kerberos
Event Xml: &lt;Event xmlns=&quot;http://schemas.microsoft.com/win/2004/08/events/event&quot;&gt;
  &lt;System&gt;     &lt;Provider Name=&quot;Microsoft-Windows-WinRM&quot; Guid=&quot;{A7975C8F-AC13-49F1-87DA-5A984A4AB417}&quot; /&gt;     &lt;EventID&gt;166&lt;/EventID&gt;     &lt;Version&gt;0&lt;/Version&gt;     &lt;Level&gt;4&lt;/Level&gt;
    &lt;Task&gt;7&lt;/Task&gt;    &lt;Opcode&gt;0&lt;/Opcode&gt;       &lt;Keywords&gt;0x400000000000000a&lt;/Keywords&gt;
    &lt;TimeCreated SystemTime=&quot;2015-01-20T14:45:36.679879800Z&quot; /&gt;      &lt;EventRecordID&gt;108887&lt;/EventRecordID&gt;
    &lt;Correlation ActivityID=&quot;{02D14C50-F800-0002-7BBA-24BE3931D001}&quot; /&gt;
    &lt;Execution ProcessID=&quot;1016&quot; ThreadID=&quot;1548&quot; /&gt;       &lt;Channel&gt;Microsoft-Windows-WinRM/Operational&lt;/Channel&gt;
    &lt;Computer&gt;Shark. LOCAL&lt;/Computer&gt;       &lt;Security UserID=&quot;S-1-5-20&quot; /&gt;
  &lt;/System&gt;  &lt;EventData&gt;    &lt;Data Name=&quot;auth&quot;&gt;Kerberos&lt;/Data&gt;

Log Name:      Microsoft-Windows-WinRM/Operational   Source:        Microsoft-Windows-WinRM
Date:          1/20/2015 9:45:36 AM    Event ID:      129
Task Category: Response handling               Level:         Error        Keywords:      Client
User:          NETWORK SERVICE           Computer:      Shark.local
Description:  Received the response from Network layer; status: 401 (HTTP_STATUS_DENIED)
Event Xml: &lt;Event xmlns=&quot;http://schemas.microsoft.com/win/2004/08/events/event&quot;&gt;
  &lt;System&gt;    &lt;Provider Name=&quot;Microsoft-Windows-WinRM&quot; Guid=&quot;{A7975C8F-AC13-49F1-87DA-5A984A4AB417}&quot; /&gt;    &lt;EventID&gt;129&lt;/EventID&gt;    &lt;Level&gt;2&lt;/Level&gt;     &lt;Task&gt;10&lt;/Task&gt;
    &lt;Opcode&gt;1&lt;/Opcode&gt;     &lt;Keywords&gt;0x4000000000000002&lt;/Keywords&gt;
    &lt;TimeCreated SystemTime=&quot;2015-01-20T14:45:36.679879800Z&quot; /&gt;
    &lt;EventRecordID&gt;108888&lt;/EventRecordID&gt;
    &lt;Correlation ActivityID=&quot;{02D14C40-F800-0000-25BD-24BE3931D001}&quot; /&gt;
    &lt;Execution ProcessID=&quot;1016&quot; ThreadID=&quot;1432&quot; /&gt;
    &lt;Channel&gt;Microsoft-Windows-WinRM/Operational&lt;/Channel&gt;
    &lt;Computer&gt;Shark. &lt;/Computer&gt;     &lt;Security UserID=&quot;S-1-5-20&quot; /&gt;
  &lt;/System&gt;   &lt;EventData&gt;     &lt;Data Name=&quot;status&quot;&gt;401 (HTTP_STATUS_DENIED)&lt;/Data&gt;</code></pre><p>Is this an error caused by our Wireshark configuration and if so what can we do to eliminate it? The error was not showing on the machine before Wireshark was installed. We also get similar errors on the responding PC.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-error129" rel="tag" title="see questions tagged &#39;error129&#39;">error129</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '15, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/335a4f7aece34347a961f94bb087d6ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KPL&#39;s gravatar image" /><p><span>KPL</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KPL has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '15, 09:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39317" class="comments-container"></div><div id="comment-tools-39317" class="comment-tools"></div><div class="clear"></div><div id="comment-39317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39319"></span>

<div id="answer-container-39319" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39319-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39319-score" class="post-score" title="current number of votes">0</div><span id="post-39319-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The event log entries are for WinRM, a remoting mechanism used in newer version of Windows.</p><p>I think it's entirely unrelated to Wireshark itself, more likely due to the environment, in that the captures are probably putting the NIC into promiscuous mode to capture all traffic and the switch is set up to span or mirror all traffic onto the capture port.</p><p>The usual recommendation for a "pure" capture device is to remove all transport bindings from the NIC used for capture so that "normal" traffic won't be seen in the capture, this might stop the event log entries, but personally I don't think they're worth worrying about.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '15, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39319" class="comments-container"></div><div id="comment-tools-39319" class="comment-tools"></div><div class="clear"></div><div id="comment-39319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

