import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HomepageurlComponent } from './homepageurl.component';

describe('HomepageurlComponent', () => {
  let component: HomepageurlComponent;
  let fixture: ComponentFixture<HomepageurlComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HomepageurlComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomepageurlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
