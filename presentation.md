Using Mojolicious for Fun and Nonprofit

[Lee Johnson](http://leejo.github.io)

September 2014

---
## About Me?

---
## About Me?

+ Perl developer for 10+ years

---
## About Me?

+ Perl developer for 10+ years
+ Occasional contributor to CPAN

---
## About Me?

+ Perl developer for 10+ years (sometimes Python/C)
+ Occasional contributor to CPAN
+ More active recently:
    - Uploading to CPAN ([pause: LEEJO](https://metacpan.org/author/LEEJO))
    - Forky forky ([github: leejo](https://github.com/leejo))
    - Primary maintainer of CGI.pm
    - This!

---
## About Me?

+ Perl developer for 10+ years
+ Occasional contributor to CPAN
+ More active recently:
    - Uploading to CPAN ([pause: LEEJO](https://metacpan.org/author/LEEJO))
    - Forky forky ([github: leejo](https://github.com/leejo))
    - Primary maintainer of CGI.pm
    - This!
+ Moved to Suisse mid-2013

---
# Nonprofit?


---
## GivenGain Group Services


---
# Fun?

+ Modern perl development tools
    * Moose/Moo/Mouse
    * DBIx::Class
    * Web Frameworks
    * Test::*
    * perlbrew/plenv/Pinto/Carton/etc
+ Modern development methods
    * Distributed VCS (git)
    * Code reviews
    * Continuous Build/Deployment
    * Automated systems infrastructure (AWS)
    * Workshops and training

---
# Not Fun.

+ "Legacy" perl code
    * No strict or warnings
    * Global variables
    * Poor separation of concerns
    * Own templating language/syntax
    * No real use of perl idioms
    * No automated tests
    * System/Vendor supplied perl

---
# This is not *bad* code

+ Running without problem for 10 years
+ Almost $100million raised for causes

It's just not fun code to work with.

---
So how do we make this fun?

+ Address previous problems in existing code?
    * No.
    * difficult because:

+ Re-write the app from the ground up?
    * Heck no!
    * I shouldn't have to explain why...

+ Gradually migrate functionality into new system?
    * That might work...

---
# Mojolicious?

---
# Why Not?

+ Dancer(2)
+ Catalyst

---
## Mojolicious::Lite

```perl
    #!/usr/bin/env perl

    # automatically enables strict, warnings, utf8 and 5.10 features
    use Mojolicious::Lite;

    any '/hello_world' => sub {
        my ( $self ) = @_;
        $self->render( text => "Bonjour à tous" );
    };

    app->start;
```

---
## CGI.pm and Mojolicious?

---
## Mojolicious Lessons Learnt

---
## Mojolicious Lessons Learnt

Mojolicious moves fast

![Mojo changes 2014](/img/mojo_changes.png)

---
## Mojolicious Lessons Learnt

Mojolicious documentation

---
## Mojolicious Lessons Learnt

Mojolicious defaults (config, exception pages, etc)
